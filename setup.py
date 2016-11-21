from distutils.core import setup, Extension
import numpy as np

module1 = Extension('_dpcore_py',
                    include_dirs = [np.get_include()],
                    sources = ['dpcore_py.c'])

setup (name = '_dpcore_py',
       version = '0.0',
       description = 'Dynamic programming core routine',
       ext_modules = [module1])
