# -*- coding: utf-8 -*-

from plot_ischemia import plot_ischemia
import os
from config_files import read_run_config_json

def run(opt, plot, save, sliders, dir_path, name):
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
    p = plot_ischemia(opt, plot, sliders)
    if save:
        save_geom(p, dir_path, name)


def save_geom(mesh, dir_path, name):
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
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = os.path.join(dir_path, name)

    if os.path.exists(file_path):
        overwrite = input("The file already exists. Do you want to overwrite it? (yes/no)")
        if overwrite == "no":
            new_filename = input("Enter the new file name:")
            while os.path.exists(os.path.join(dir_path, new_filename)):
                new_filename = input("The file already exists. Enter another name:")
            file_path = os.path.join(dir_path, new_filename)

    mesh.save(file_path)



if __name__  == '__main__':

    run_params = read_run_config_json(path=os.getcwd())['data']
    run(**run_params)
