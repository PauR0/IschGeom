# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:31:37 2023

@author: Angela
"""

opt = 'ellipse'

DEFAULT_OPTIONS_ISC = {
    
    'norm' : {
    'mu1': {
        'value': 2,
        'range': [0.01, 4],
        'title': 'Mu1'
    },
    'mu2': {
        'value': 2,
        'range': [0.01, 4],
        'title': 'Mu2'
    },
    'sigma1': {
        'value': 1,
        'range': [0.01, 4],
        'title': 'Sigma1'
    },
    'sigma2': {
        'value': 1,
        'range': [0.01, 4],
        'title': 'Sigma2'
    },
    'altura1': {
        'value': 3,
        'range': [0, 6],
        'title': 'Altura1'
    },
    'altura2': {
        'value': 1,
        'range': [0, 6],
        'title': 'Altura2'
    },
    'amplitud1': {
        'value': 4,
        'range': [1, 10],
        'title': 'Amplitud1'
    },
    'amplitud2': {
        'value': 4,
        'range': [1, 10],
        'title': 'Amplitud2'
    }
    },
    

    'ellipse' : {
    'radio1': {
        'value': 1,
        'range': [0.01, 3],
        'title': 'Radio1'
    },
    'radio2': {
        'value': 1,
        'range': [0.01, 3],
        'title': 'Radio2'
    },
    'ycenter': {
        'value': 2,
        'range': [0.01, 4],
        'title': 'Y Center'
    },
    'zcenter': {
        'value': 2,
        'range': [0.01, 6],
        'title': 'Z Center'
    }
    },     
    
    
    'cos' : {
    'min_lower': {
        'value': 2,
        'range': [0.01, 10],
        'title': 'Min Lower'
    },
    'min_upper': {
        'value': 4,
        'range': [0.01, 10],
        'title': 'Min Upper'
    },
    'scale_lower': {
        'value': 1,
        'range': [0.01, 2],
        'title': 'Scale Lower'
    },
    'scale_upper': {
        'value': 1,
        'range': [0.01, 2],
        'title': 'Scale Upper'
    },
    'curviness_lower': {
        'value': 1,
        'range': [0.01, 2],
        'title': 'Curv Lower'
    },
    'curviness_upper': {
        'value': 1,
        'range': [0.01, 2],
        'title': 'Curv Upper'
    }
     },     
    
    'sin' : {
    'min_lower': {
        'value': 2,
        'range': [0.01, 10],
        'title': 'Min Lower'
    },
    'min_upper': {
        'value': 4,
        'range': [0.01, 10],
        'title': 'Min Upper'
    },
    'scale_lower': {
        'value': 1,
        'range': [0.01, 2],
        'title': 'Scale Lower'
    },
    'scale_upper': {
        'value': 1,
        'range': [0.01, 2],
        'title': 'Scale Upper'
    },
    'curviness_lower': {
        'value': 1,
        'range': [0.01, 2],
        'title': 'Curv Lower'
    },
    'curviness_upper': {
        'value': 1,
        'range': [0.01, 2],
        'title': 'Curv Upper'
    }
     },    
    
     'hyperboloid':{
         'ycenter': {
         'value': 2,
         'range': [0.01, 4],
         'title': 'Y Center'
     },
     'zcenter': {
         'value': 3,
         'range': [0.01, 6],
         'title': 'Z Center'
     },
     'semiax1': {
         'value': 1,
         'range': [0.01, 2],
         'title': 'Semiax1'
     },
     'semiax2': {
         'value': 1,
         'range': [0.01, 2],
         'title': 'Semiax2'
    }
     },
     'amorphous_circ': {
        'radio' : {
         'value': 1,
         'range': [0.01, 2],
         'title': 'Radio'},

        'a' : {
         'value': 5,
         'range': [0, 10],
         'title': 'Frecuencia'},

        'b' :  {
         'value': 0.1,
         'range': [0, 0.5],
         'title': 'Amplitud'},

        'ycenter': {
         'value': 2,
         'range': [0.01, 4],
         'title': 'Y Center'},

        'zcenter': {
         'value': 2,
         'range': [0.01, 6],
         'title': 'Z Center'
    }
    
     }
}

