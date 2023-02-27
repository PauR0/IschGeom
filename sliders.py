# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:53:18 2023

@author: Angela
"""

from ischemia import DEFAULT_OPTIONS_ISC
import plotischemia


class SliderRoutine:  
    def __init__(self, opt, mesh):
        KWARGS_ISC = {
        name: DEFAULT_OPTIONS_ISC[opt][name]['value'] for name in DEFAULT_OPTIONS_ISC[opt].keys()
        }
        self.output = mesh
        self.kwargs = KWARGS_ISC

    def __call__(self, param, value, opt):
        self.kwargs[param] = value
        self.update(opt)

    def update(self, opt):
        result = plotischemia.grid_updatter(opt, self.kwargs)
        self.output.copy_from(result)  


def add_sliders(opt, plotter, mesh):
    """Create a set of slider widgets to control the parameters 
    depending on the ischemia zone.

    Args:
    ----
        opt : str
            Type of geometry to use for the simulation.
        plotter : pyvista.Plotter
            The plotter object on which the sliders will be added.
        mesh : pyvista.StructuredGrid
            The mesh representing the ischemia simulation.
    """
    slider_engine = SliderRoutine(opt, mesh)

    i = 0
    for key, val in DEFAULT_OPTIONS_ISC[opt].items():
        xcoord = 0.025 + 0.15 * (i % 6)
        ycoord = 0.1 if i < 6 else 0.3

        plotter.add_slider_widget(
        # bound_key=key evita problemes de 'scoping'
            callback=lambda v, bound_key=key: slider_engine(bound_key, v, opt),
            rng=val['range'],
            value=val['value'],
            title=val['title'],
            pointa=(xcoord, ycoord),
            pointb=(xcoord + 0.1, ycoord),
            style='modern'
        )

        i += 1
        