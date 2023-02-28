import os

import argparse

import numpy as np

import pyvista as pv

import elvira_base_files as ebf

def load_mesh(fname):

    if not fname.endswith('.vtk'):
        print("Wrong file given, only *.vtk files are read....")
        return

    mesh = pv.read(fname)
    return mesh
#

def make_elvira_nodes_file(mesh, dest, w=False):

    fout = dest+'/nodes.dat'

    if os.path.exists(fout) and not w:
        print(f"Warning {fout} already exists and overwriting is set to false, nothing will be written....")
        return None

    with open(fout, 'w') as nf:
        nf.write(f'{mesh.points.shape[0]}  1  {mesh.points.shape[1]}\n')
        nf.write(f'{mesh.points.shape[0]} NODETYPE\n')
        for i, p in enumerate(mesh.points):
            l = f"   {i+1}\t {int(mesh['Endo2Epi'][i])}\t "
            for x in p:
                l+=f'{x} '
            l+='\n'
            nf.write(l)

    return fout
#

def make_elvira_elements_file(mesh, dest, w=False):

    fout = dest+'/elements.dat'

    if os.path.exists(fout) and not w:
        print(f"Warning {fout} already exists and overwriting is set to false, nothing will be written....")
        return None

    with open(fout, 'w') as f:
        n_elem = mesh.cells_dict[12].shape[0]
        n_elem_types = len(np.unique(mesh.celltypes)) #Currently only hexahedra are supported
        f.write(f'{n_elem} {n_elem_types}\n')
        f.write(f'{n_elem} HT3DH08\n')
        for i, p in enumerate(mesh.cells_dict[12]):
            l = f"   {i+1}\t {int(mesh['Cell_type'][i])}\t "
            for x in p:
                l+=f'{int(x)} '
            l+='\n'
            f.write(l)

    return fout
#

def make_elvira_fibre_file(mesh, dest, w=False):

    fout = dest+'/fibre.dat'

    if os.path.exists(fout) and not w:
        print(f"Warning {fout} already exists and overwriting is set to false, nothing will be written....")
        return None

    with open(fout, 'w') as f:

        f.write('3 \n')

        cell_types = 1 + np.arange(mesh['Cell_type'].max())
        for i in cell_types:
            l = f"   {int(i)}\t {int(i)}\t 0\t 3\t {0.0} {1.0} {0.0}"
            f.write(l)

    return fout
#

def make_elvira_material_file(dest):

    mat_text = ebf.materials
    fout = dest+'/materials.dat'
    with open(fout, 'w') as f:
        f.write(mat_text)

    return fout
#

def make_elvira_stimulus_file(mesh, dest, S1=600.0, n_stim=10, w=False, debug=False):


    fout = dest+'/stimuli.dat'

    if os.path.exists(fout) and not w:
        print(f"Warning {fout} already exists and overwriting is set to false, nothing will be written....")
        return None


    sel_ids = np.argwhere(mesh.points[:,1] == 0).flatten()

    with open(fout, 'w') as f:
        f.write('1 \n')
        l = f" 1 {int(n_stim)} "
        for i in range(n_stim):
            l+=f" {i*S1} 2.0 100.0"
        f.write(l)

        l = f"  {sel_ids.shape[0]} 0"
        f.write(l)

        print(f"Last stimulus will trigger at {(n_stim-1)*S1} ....")

        for i in sel_ids:
            l = f"   {i} 1"
            f.write(l)

    if debug:
        sc = np.zeros(mesh.points.shape)
        sc[sel_ids] = 1
        p = pv.Plotter()
        p.add_mesh(mesh, scalars=sc)
        p.show()

    t_max = (n_stim-1)*S1 + 400
    return t_max
#

def make_elvira_main_file(name, t_max, dest, w=False):
    """
    TODO: Documentation
    """

    main_text = ebf.main.replace("**TMAX**", f"{t_max:.2f}")
    main_text = ebf.main.replace("**NAME**", name)
    fout = dest+'/main_file.dat'
    with open(fout, 'w') as f:
        f.write(main_text)

    return fout
#

def make_post_config_file():
    """
    TODO: Finish the func and document
    """
    pc_text = ebf.post_conf
    #


def vtk_to_elv_data(orig, dest=None, w=False):

    mesh = load_mesh(orig)

    path, name = os.path.split(orig)
    if not path:
        path='.'

    if dest is None:
        save_dir = path+'/data'
    else:
        save_dir = dest

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    make_elvira_nodes_file(mesh, dest=save_dir, w=w)
    make_elvira_elements_file(mesh, dest=save_dir, w=w)
    make_elvira_fibre_file(mesh, dest=save_dir, w=w)
    t_max = make_elvira_stimulus_file(mesh, dest=save_dir, w=w)
    make_elvira_main_file(name, t_max, dest=save_dir, w=w)
    make_elvira_material_file(dest)
    make_post_config_file()
#

if __name__ == '__main__':

    #TODO: Update Parser and doc
    parser = argparse.ArgumentParser(description=""" Module to make ELVIRA cases from vtk unstructured grids. """,
                                    usage = """ """)

    parser.add_argument('-w',
                        '--overwrite',
                        dest='w',
                        action='store_true',
                        help=""" Overwrite existing files.""")

    parser.add_argument('-d',
                        '--dest',
                        '--destination',
                        dest='dest',
                        type=str,
                        nargs='?',
                        help="""Directory to save the nodes.dat file.""")

    parser.add_argument('path',
                        action='store',
                        type=str,
                        nargs='?',
                        help="""Path to an existing case of cases.""")


    args = parser.parse_args()

    vtk_to_elv_data(orig=args.path, dest=args.dest, w=args.w)