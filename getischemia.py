# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:40:16 2023

@author: Angela
"""

import numpy as np

def get_ids(opt, points, d):
    """
    Returns a boolean array indicating which points are within the ischemia zone.

    Args:
    ----
        opt : str
            Type of geometry to use for the simulation.
        points: np.ndarray
            An array of shape (n,3) containing the coordinates of each point in the mesh.
        d: dict
            A dictionary with the ischemia parameters.

    Returns:
    -------
        np.ndarray : 
            A boolean array of shape (n,3) where True values indicate 
            that the corresponding point is within the ischemia zone.

    """
    if opt == 'norm': 
        mu1 = d['mu1']
        mu2 = d['mu2']
        sigma1 = d['sigma1']
        sigma2 = d['sigma2']
        altura1 = d['altura1']
        altura2 = d['altura2']
        amplitud1 = d['amplitud1']
        amplitud2 = d['amplitud2']
    
        normal_func1 = lambda x: (np.e**(-(1/2)*((x-mu1)**2)/sigma1**2))/(sigma1*np.sqrt(2*np.pi))
        normal_func2 = lambda x: (np.e**(-(1/2)*((x-mu2)**2)/sigma2**2))/(sigma2*np.sqrt(2*np.pi))

        grid_values1 = normal_func1(points[:,1])
        grid_values2 = normal_func2(points[:,1])

        return np.logical_and(points[:,2] < amplitud1*grid_values1 + altura1, points[:,2] > amplitud2*grid_values2 + altura2)
    
       
    if opt == 'ellipse':
        radio1 = d['radio1']
        radio2 = d['radio2']
        zcenter = d['zcenter']
        ycenter = d['ycenter']
        return (np.sqrt(((points[:, 2]-zcenter)**2)/(radio2**2)+((points[:, 1]-ycenter)**2)/(radio1**2)) <= 1)
    
    if opt == 'cos':
        curviness_lower = d['curviness_lower']
        scale_lower = d['scale_lower']
        min_lower = d['min_lower']
        curviness_upper = d['curviness_upper']
        scale_upper = d['scale_upper']
        min_upper = d['min_upper']
        return np.logical_and(
        points[:, 2] >= np.cos(
            points[:, 1]*curviness_lower
        )*scale_lower + min_lower,
        points[:, 2] <= np.cos(
            points[:, 1]*curviness_upper
        )*scale_upper + min_upper)
    
    if opt == 'sin':
        curviness_lower = d['curviness_lower']
        scale_lower = d['scale_lower']
        min_lower = d['min_lower']
        curviness_upper = d['curviness_upper']
        scale_upper = d['scale_upper']
        min_upper = d['min_upper']
        return np.logical_and(
        points[:, 2] >= np.sin(
            points[:, 1]*curviness_lower
        )*scale_lower + min_lower,
        points[:, 2] <= np.sin(
            points[:, 1]*curviness_upper
        )*scale_upper + min_upper)
        
    if opt == 'hyperboloid':
        semiax1 = d['semiax1']
        semiax2 = d['semiax2']
        zcenter = d['zcenter']
        ycenter = d['ycenter']
        return ((points[:,2]-zcenter)**2/(semiax2**2) - (points[:,1]-ycenter)**2/(semiax1**2) <= 1)
    
    if opt == 'amorphous_circ':
        radio = d['radio']
        a = d['a']
        b = d['b']
        zcenter = d['zcenter']
        ycenter = d['ycenter']
        distances_to_center = np.sqrt((points[:,2]-zcenter)**2 + (points[:,1]-ycenter)**2)
        r = np.random.normal(radio, 0, points.shape[0]) + np.sin(points[:, 1]*a)*b
        return distances_to_center <= r

def get_scalars(opt, points, d):
    """
    This function calculates the scalar values for each point 
    in a mesh based on a given dictionary of ischemia zones.

    Args:
    ----
        opt : str
            Type of geometry to use for the simulation.
        points : numpy.ndarray
            An array of shape (n, 3) containing the coordinates of each point in the mesh.
        d : dict
            A dictionary with the ischemia parameters.

    Returns:
    -------
        numpy.ndarray : 
        An array of shape (n,3) containing the scalar values assigned to each point in the mesh. 
        Points inside the ischemia zones are assigned a value of 1, 
        while points outside the zones are assigned a value of 0.
    """

    scalars = np.zeros((points.shape[0],))

    ids = get_ids(opt, points, d)
    scalars[ids] = 1
    return scalars