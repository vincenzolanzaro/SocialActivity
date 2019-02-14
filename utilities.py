# -*- coding: utf-8 -*-
import sys
import os.path
import importlib
import threading

class utilities:
    #def __init__(self):

    #-----------------------------------------------------------------------
    # importModule is a function created for Python 3.5+ to import top-level
    # module (that is not a file but is packaged as a directory with __init__.py)
    # and all its IMPORTs (something that quite often create problems)
    #-----------------------------------------------------------------------
    def importModule(self, moduleName=None, modulePath=None):
        fullPath = os.path.dirname(os.path.realpath(__file__)) + modulePath
        print(fullPath)
        spec = importlib.util.spec_from_file_location(moduleName, fullPath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module 
        spec.loader.exec_module(module)
        #print(dir(module)) use it to see if module is perfectly loaded
        return module


    def run_threaded(self, job_fn, thread_join = False):
        #function to make threads -> details here http://bit.ly/faq_schedule
        job_thread=threading.Thread(target=job_fn)
        job_thread.daemon = True
        job_thread.start()
        if thread_join:
            job_thread.join()