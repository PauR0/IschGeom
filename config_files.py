#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
import json

default_run_json = {
    "metadata" : {
        'type' : 'run',
        'version' : 0.01
    },
    'data' :{
        "opt" : "norm",
        "save" : True,
        "plot" : True,
        "sliders" : True,
        "dir_path" : "geomsvtk",
        "name" : "geom.vtk"
    }
}


def pretty_write(j,
                 f,
                 write_replacements = [[',',',\n'],
                                ['}}','}\n }'],
                                ['{"','{\n "'],
                                ['"}','"\n}']]):
    for r in write_replacements:
        j = j.replace(r[0],r[1])
    j += "\n"
    f.write(j)
#


def read_json(file):
    params = None
    with open(file) as param_file:
        params = json.load(param_file)

    #
    return params
#

def get_json_reader(json_filename,template):

    params = deepcopy(template)
    fname = json_filename

    def read_json(path=None,abs_path=False):

        new_params = deepcopy(params)
        try:
            if abs_path:
                json_file = path
            else:
                json_file = path + "/" + fname

            with open(json_file) as param_file:
                read_params = json.load(param_file)
                for k in read_params['metadata']:
                    new_params['metadata'][k] = read_params['metadata'][k]
                for k in read_params['data']:
                    new_params['data'][k] = read_params['data'][k]
        except (FileNotFoundError,TypeError):
            pass
        #

        return new_params
    #

    return read_json
#

def get_json_writer(json_filename,template):

    params = deepcopy(template)
    fname = json_filename

    def write_json(path,data=None,abs_path=False):

        if abs_path:
            json_file = path
        else:
            json_file = path + "/" + fname

        try:
            with open(json_file,'w') as param_file:
                if data:
                    for k in data['metadata']:
                        params['metadata'][k] = data['metadata'][k]
                    for k in data['data']:
                        params['data'][k] = data['data'][k]
                pretty_write(json.dumps(params, indent=4), param_file)
        except FileNotFoundError:
            pass
        #

        return params
    #

    return write_json
#


read_run_config_json = get_json_reader("run_config.json",
                                        default_run_json)

write_run_config_json = get_json_writer("run_config.json",
                                          default_run_json)