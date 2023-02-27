# -*- coding: utf-8 -*-

from plot_ischemia import plot_ischemia
import os
import json
from df_json import DEFAULT_JSON as dfj

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

def read_json(dt, dfj):
    """
    Reads a JSON file and, if a value in the file is None,
    it is replaced by the corresponding value by default.

    Args:
        dt : dict
            A dict with the values of the JSON file.
        dfj : dict
            A dict with the default values.

    Returns:
        dict :
            The dictionary with updated values.
    """
    for key, value in dt.items():
        if value == None:
            dt[key] = dfj[key]
    return dt


if __name__  == '__main__':
    json_file = r'g1.json'

    if (os.path.exists(json_file)) and (os.path.getsize(json_file) > 0):
            with open(json_file, 'r') as f:
                data = json.load(f)
                data = read_json(data, dfj)
            run(**data)
    else:
        run(**dfj)
