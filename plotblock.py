# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:36:11 2023

@author: Angela
"""
import numpy as np
import pyvista as pv
from block import DEFAULT_KWARGS_BLOCK


def create_grid_mesh(sx=DEFAULT_KWARGS_BLOCK['sx'], sy=DEFAULT_KWARGS_BLOCK['sy'], sz=DEFAULT_KWARGS_BLOCK['sz'],
                     dx=DEFAULT_KWARGS_BLOCK['dx'], dy=DEFAULT_KWARGS_BLOCK['dy'], dz=DEFAULT_KWARGS_BLOCK['dz']):

    """
    Creates a structured grid mesh using the given dimensions and spacing values.
    
    Args:
    ----
        sx : float, optional
            Size of the mesh in the x direction. Default is set to 'DEFAULT_KWARGS_BLOCK['sx']'.
        sy : float, optional
            Size of the mesh in the y direction. Default is set to 'DEFAULT_KWARGS_BLOCK['sy']'.
        sz : float, optional
            Size of the mesh in the z direction. Default is set to 'DEFAULT_KWARGS_BLOCK['sz']'.
        dx : float, optional
            Spacing between points in the x direction. Default is set to 'DEFAULT_KWARGS_BLOCK['dx']'.
        dy : float, optional
            Spacing between points in the y direction. Default is set to 'DEFAULT_KWARGS_BLOCK['dy']'.
        dz : float, optional
            Spacing between points in the z direction. Default is set to 'DEFAULT_KWARGS_BLOCK['dz']'.
        
    Returns:
    -------
        pv.StructuredGrid :
            A 'pyvista.StructuredGrid' object representing the mesh.
    """

    nx = round(sx/dx)
    ny = round(sy/dy)
    nz = round(sz/dz)

    xrng = np.linspace(0, sx, nx, dtype=np.float32)
    yrng = np.linspace(0, sy, ny, dtype=np.float32)
    zrng = np.linspace(0, sz, nz, dtype=np.float32)
    x, y, z = np.meshgrid(xrng, yrng, zrng)

    return pv.StructuredGrid(x, y, z)

def plot_block():
    """
    Creates an empty plotter using PyVista and a 3D structured grid mesh 
    using the create_grid_mesh function.
    
    Returns:
    -------
        tuple(pv.StructuredGrid, pv.Plotter) :
            A tuple containing the 'pyvista.StructuredGrid' object representing 
            the mesh and the 'pyvista.Plotter' object used to plot it.
    """

    plotter = pv.Plotter()
    grid_mesh = create_grid_mesh()
    
    return grid_mesh, plotter


