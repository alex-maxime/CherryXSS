# Initial server source code from Jovan Brakus (jovan@brakus.rs) (Many thanks for showing me a great scaffold for CherryPy)
# All levels of the XSS challenge are under the MIT license; Good luck learning!
# Follow me on twitter @infosec_au or take a visit to http://shubh.am
import cherrypy
class l1(object):
    @cherrypy.expose
    def index(self):
        host = cherrypy.request.headers['Host']
        ua = cherrypy.request.headers['User-Agent']
        ip = cherrypy.request.remote.ip
        #c_length = cherrypy.request.headers['Content-Length']
        return """
<!doctype html>
<html>
  
  <head>
    <title>Level 1</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
    <link rel="stylesheet" href="../static/css/bootstrap.css">
    <link rel="stylesheet" href="../static/css/bootstrap-responsive.css">
    <link rel="stylesheet" href="../static/css/flat-ui.css">
    <script src="../static/js/jquery.min.js"></script>
    <script src="../static/js/bootstrap.min.js"></script>
  </head>
  <!-- seriously guys/girls, this isn't a 1990s hacking game with shit hidden in the source code. If you need a tip or help, visit the walkthroughs. Cheers, and good luck. -->
  <body>
    <div class="container">
      <div class="pagination pagination-large pagination-centered">
        <div class="well well-large">
          <div class="hero-unit">
            <h1>XSS Challenge 1
              <br> 
            </h1>
            <p>Welcome.
              <br> 
            </p>
            <p>Your user-agent is: """ + ua + """
              <br> 
            </p>
            <p>Host: """ + host + """
              <br> 
            </p>
            <p>IP: """ + ip + """
              <br> 
            </p>
            <p class="align-left">Your aim in this challenge is to execute javascript. Once done, please
              direct yourself to the next challenge. While the walkthrough button is
              tempting, please have at least
              <u><b>5</b></u> attempts before clicking it.
              <br> 
            </p>
            <p style="" class="pull-left">
              <br> 
            </p>
            <p></p>
            <p>
              <a href="/walkthrough1" class="btn btn-primary btn-large">Walkthrough</a> 
            </p>
                    <a href="/level2" class="btn">Next Challenge</a> 
          </div>
    </div>
  </body>

</html>
"""
class w1(object):
    @cherrypy.expose
    def index(self):
        return """<!doctype html>
<html>
  
  <head>
    <title>Walkthrough 1</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
    <link rel="stylesheet" href="../static/css/bootstrap.css">
    <link rel="stylesheet" href="../static/css/bootstrap-responsive.css">
    <link rel="stylesheet" href="../static/css/flat-ui.css">
    <script src="../static/js/jquery.min.js"></script>
    <script src="../static/js/bootstrap.min.js"></script>
  </head>
  
  <body>
    <div class="container">
      <div class="pagination pagination-large pagination-centered">
        <div class="well well-large">
          <div class="hero-unit">
            <h1>Walkthrough&nbsp; 1
              <br> 
            </h1>
            <p class="align-left">Welcome.&nbsp; XSS is also commonly known as cross site scripting. It
              is basically, when unfiltered user input, in any way possible is able to
              inject javascript into the web application. The method if inserting the
              JS, is not always straightforward and requires people to think outside
              the box. Sometimes, the web applications will
              <u><b>ATTEMPT</b></u> to filter out certain characters to prevent XSS, but obviously, there
              are often workarounds.
              <br> 
            </p>
            <p>Now for Challenge 1:
              <br> 
            </p>
            <p class="align-left">1. Get LiveHTTPHeaders or Tamper Data as a firefox addon.
              <br> 
            </p>
            <p class="align-left">2. In this case, I will be demonstrating LiveHTTPHeaders: this addon is
              able to replay what our browser has sent, while being able to modify certain
              parameters not normally modifiable from the front end. For example, on
              LiveHTTPHeaders, open it up and make sure the "capture" box is ticked.
              <br> 
            </p>
            <p class="align-left">3. Visit our XSS challenge 1 page and seek out where the data is ON LiveHTTPHeaders.
              Once found, click it and then click "Replay"
              <br> 
            </p>
            <p class="align-left">4. Now you can edit so much more. Try inserting a simple alert into the
              User-Agent field and execute it.
              <br> 
            </p>
            <p class="align-left">5. Well done. You have just XSS'd your first page (presumably)
              <br> 
            </p>
            <p style="" class="pull-left">
              <br> 
            </p>
            <p></p>
            <p></p>
            <a href="/level2" class="btn">Next Challenge</a> 
          </div>
        </div>
      </div>
    </div>
  </body>

</html>"""
