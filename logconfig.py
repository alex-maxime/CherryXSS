#!/usr/bin/env python

#!/usr/bin/python
# Initial server source code from Jovan Brakus (jovan@brakus.rs) (Many thanks for showing me a great scaffold for CherryPy)
# All levels of the XSS challenge are under the MIT license; Good luck learning!
# Follow me on twitter @infosec_au or take a visit to http://shubh.am

import os
import sys
import logging
import logging.handlers

DEFAULT_LOG_LEVEL = logging.DEBUG
LOG_DIR = 'logs'
LOG_FILENAME = 'cherrypy-server.log'
    
def init_logging():
    # get root and readings logger, and remove default handlers -- we set our own
    try:
        if not os.path.exists(LOG_DIR):
            print "Log folder %s doesn't exist. Creating it..." % LOG_DIR
            os.makedirs(LOG_DIR)
    except:
        print 'Failed to create log directory: %s' % LOG_DIR
        sys.exit(2)
    
    root_log = logging.getLogger()
    if root_log.handlers:
        for handler in root_log.handlers:
            root_log.removeHandler(handler)
    
    root_handler = logging.handlers.RotatingFileHandler(os.path.join(LOG_DIR, LOG_FILENAME), maxBytes=20971520, backupCount=50)
    root_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")    
    root_handler.setFormatter(root_formatter)    
    root_log.addHandler(root_handler)    
    root_log.setLevel(DEFAULT_LOG_LEVEL)
    
#Run log initialization function only once, first time module is loaded into memory
logInitDone=False
if not logInitDone:
    logInitDone = True
    init_logging()