"""
CherryPy Config server settings module.
"""

__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

CONFIG_FILENAME = "config_server.ini"
WEBSERVER_HOST = '0.0.0.0'
WEBSERVER_PORT = 8080
USERS = {'xssdemo': 'af1f13aa58241412f19b62502f2f31c1f290789b'} # SHA1 hash for 'xssdemo' 
LOG_DIR = 'logs'
TEMP_DIR = 'temp'
