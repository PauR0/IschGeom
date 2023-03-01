# -*- coding: utf-8 -*-

from plot_ischemia import plot_ischemia
import os
import json
from config_files import read_run_config_json, write_run_config_json

def run(run_params):
    """
    Runs the ischemia simulation and saves the resulting mesh if specified.

    Args:
    ----
        opt : str
            Type of geometry to use for the simulation.
        plot : bool
            If True, displays the plot.
        save : bool
            If True, saves the mesh.
        sliders : bool
            If True, adds sliders to control the simulation parameters interactively.
        dir_path : str
            Path to the directory where the mesh will be saved.
        name : str
            Name of the file where the mesh will be saved.
    """
    p, upd_v = plot_ischemia(run_params['opt'], run_params['plot'], run_params['sliders'])
    if run_params['save']:
        save_geom(p, upd_v, run_params)


def save_geom(mesh, upd_v, run_params):
    """
    Saves the mesh to a VTK file.

    Args:
    ----
        mesh : pyvista.StructuredGrid
            The mesh to be saved.
        dir_path : str
            Path to the directory where the mesh will be saved.
        name : str
            Name of the file where the mesh will be saved.
    """
    if not os.path.exists(run_params['save_dir']):
        os.makedirs(run_params['save_dir'])

    file_path = os.path.join(run_params['save_dir'], run_params['case_name'])

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    elif os.path.exists(file_path):
        overwrite = input("That save path already exists. Do you want to overwrite it? (yes/no)")
        if overwrite == "no":
            new_filename = input("Enter the new path name:")
            while os.path.exists(os.path.join(run_params['save_dir'], new_filename)):
                new_filename = input("That save path already exists. Enter another name:")
            os.makedirs(os.path.join(run_params['save_dir'], new_filename))
            file_path = os.path.join(run_params['save_dir'], new_filename)
            run_params['case_name'] = new_filename

    mesh.save(os.path.join(file_path, "mesh.vtk"))
    write_run_config_json(path=file_path, json_filename = "config.json", template = run_params)
    write_run_config_json(path=file_path, json_filename = "mesh_config.json", template = upd_v)


if __name__  == '__main__':
    run_params = read_run_config_json(path=os.getcwd())['data']
    run(run_params)
