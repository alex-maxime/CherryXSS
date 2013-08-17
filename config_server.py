#!/usr/bin/python
# Initial server source code from Jovan Brakus (jovan@brakus.rs) (Many thanks for showing me a great scaffold for CherryPy)
# All levels of the XSS challenge are under the MIT license; Good luck learning!
# Follow me on twitter @infosec_au or take a visit to http://shubh.am
import sys
import logging 

#Set logging handlers for the first time
import logconfig

from configserver.web import ConfigServer

log = logging.getLogger(__name__)

def main():
	try:
		webConfigServer = ConfigServer()
		webConfigServer.start()
		return 0
	except:
		# Dump callstack to log and exit with -1
		log.exception('Unexpected exception occured.') 
		return -1
	
if __name__ == '__main__':
      sys.exit(main())

