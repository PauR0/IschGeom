# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:15:01 2023

@author: Angela
"""
from plotischemia import plot_ischemia
import pyvista as pv
import os
import json
from ischemia import opt

def run(opt, pl, save, sliders, dir_path, name):
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
    p = plot_ischemia(opt, pl, sliders = sliders)
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
    json_file = r'C:\Users\Angela\Desktop\Universidad\Cuarto\Practicas\geometria\ischemic_regions\g1.json'

    if (os.path.exists(json_file)) and (os.path.getsize(json_file) > 0):
            with open(json_file, 'r') as f:
                data = json.load(f)
            run(data["opt"], data["plot"], data["save"], data["sliders"], data["dir_path"], data["name"])
    else:
        run(opt, True, True, True, r'C:\Users\Angela\Desktop\Universidad\Cuarto\Practicas\geometria\ischemic_regions\geomsvtk', "geomi.vtk")
        