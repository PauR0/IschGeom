# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:17:22 2023

@author: Angela
"""

DEFAULT_OPTIONS_BLOCK = {
    'sx': {
        'value': 0.5,
        'range': [0.01, 10],
        'title': 'X axis'
    },
    'sy': {
        'value': 4,
        'range': [0.01, 10],
        'title': 'Y axis'
    },
    'sz': {
        'value': 6,
        'range': [0.01, 10],
        'title': 'Z range'
    },
    'dx': {
        'value': 0.03,
        'range': [0.01, 1],
        'title': 'Delta X'
    },
    'dy': {
        'value': 0.03,
        'range': [0.01, 1],
        'title': 'Delta Y'
    },
    'dz': {
        'value': 0.03,
        'range': [0.01, 1],
        'title': 'Delta Z'
    }
}

DEFAULT_KWARGS_BLOCK = {
    name: DEFAULT_OPTIONS_BLOCK[name]['value'] for name in DEFAULT_OPTIONS_BLOCK.keys()
}