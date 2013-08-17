# Initial server source code from Jovan Brakus (jovan@brakus.rs) (Many thanks for showing me a great scaffold for CherryPy)
# All levels of the XSS challenge are under the MIT license; Good luck learning!
# Follow me on twitter @infosec_au or take a visit to http://shubh.am

import os.path
import cherrypy

from sha import sha

from configserver import settings
from iniconfig import IniConfigServer
from logs import LogsServer
from root import indexserver
from level1 import l1,w1
from level2 import l2,w2
from level3 import l3,w3
from level4 import l4,w4
def encrypt_pw(pw):
    return sha(pw).hexdigest()

class ConfigServer:
    users = None
    rootServer = None
    config = None

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        static_dir = os.path.join(current_dir, '..', 'static')        

        self.config = { '/': {'tools.basic_auth.on': True,
                              'tools.basic_auth.realm': 'XSS Demo Hint[user:xssdemo & pass:xssdemo]',
                              'tools.basic_auth.users': {'xssdemo':encrypt_pw('xssdemo')},
                              'tools.basic_auth.encrypt': encrypt_pw,
                              'tools.staticdir.root': static_dir},
                        '/static': {'tools.gzip.on': True,
                                    'tools.staticdir.on': True,
                                    'tools.staticdir.dir': ''},
                        '/static/css': {'tools.gzip.mime_types':['text/css'],
                                        'tools.staticdir.dir': 'css'},
                        '/static/js': {'tools.gzip.mime_types': ['application/javascript'],
                                       'tools.staticdir.dir': 'js'},
                        '/static/img': {'tools.staticdir.dir': 'images'}}

        self.rootServer = indexserver()
        self.rootServer.level1 = l1()
        self.rootServer.walkthrough1 = w1()
        self.rootServer.level2 = l2()
        self.rootServer.walkthrough2 = w2()
        self.rootServer.level3 = l3()
        self.rootServer.walkthrough3 = w3()
        self.rootServer.level4 = l4()
        self.rootServer.walkthrough4 = w4()
        
    def start(self):
        global_conf = {'global': {'server.socket_host': settings.WEBSERVER_HOST,
                                  'server.socket_port': settings.WEBSERVER_PORT}}
        cherrypy.config.update(global_conf)        
        cherrypy.config["tools.encode.on"] = True
        cherrypy.config["tools.encode.encoding"] = "utf-8"
        cherrypy.config["tools.sessions.on"] = True
        cherrypy.tree.mount(self.rootServer, '/', config = self.config)
        cherrypy.engine.start()
        
