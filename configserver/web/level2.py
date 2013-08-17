# Initial server source code from Jovan Brakus (jovan@brakus.rs) (Many thanks for showing me a great scaffold for CherryPy)
# All levels of the XSS challenge are under the MIT license; Good luck learning!
# Follow me on twitter @infosec_au or take a visit to http://shubh.am
import cherrypy
class l2(object):
    @cherrypy.expose
    def index(self):
      return """<!doctype html>
<html>
  
  <head>
    <title>Level 2</title>
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
            <h1>XSS Challenge&nbsp; 2
              <br> 
            </h1>
            <p class="align-center">Hi there! I was wondering what your name was. Is your name 1337 h4x0r
              99_I_Hacked_the_Gibson? Woops! Did I get it wrong again? Let me know by entering it down below.
              <br> 
            </p>
            <form action="name" method="get">
              <input placeholder="Name here" name="name" class="input-medium" type="text">
              <div class="form-actions">
                <button type="submit" class="btn btn-primary">Submit</button>
                <input class="btn" value="Reset" type="reset"> 
              </div>
            </form>
            <p></p>
            <p style="" class="pull-left">
              <br> 
            </p>
            <p></p>
            <p></p>
            <p>
              <a href="/walkthrough2" class="btn btn-primary btn-large">Walkthrough</a> 
            </p>
            <a href="/level3" class="btn">Next Challenge</a> 
          </div>
        </div>
      </div>
    </div>
  </body>

</html>"""
    @cherrypy.expose
    def name(self, name):
            return """
            <!doctype html>
<html>
  
  <head>
    <title>Level 2</title>
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
            <h1>XSS Challenge&nbsp; 2
              <br> 
            </h1>
            <p class="align-center">Hi there! I was wondering what your name was. Is your name 1337 h4x0r
              99_I_Hacked_the_Gibson? Woops! Did I get it wrong again? Let me know by entering it down below.
              <br> 
            </p>
<b> HI THERE """ + str(name) + """!</b>
            <p></p>
            <p style="" class="pull-left">
              <br> 
            </p>
            <p></p>
            <p></p>
            <p>
              <a href="/walkthrough2" class="btn btn-primary btn-large">Walkthrough</a> 
            </p>
            <a href="/level3" class="btn">Next Challenge</a> 
          </div>
        </div>
      </div>
    </div>
  </body>

</html>"""
class w2(object):
    @cherrypy.expose
    def index(self):
        return """<!doctype html>
<html>
  
  <head>
    <title>Walkthrough 2</title>
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
            <h1>Walkthrough&nbsp; 2
              <br> 
            </h1>
            <p class="align-left">Welcome.&nbsp; Well.... have you ever thought of how much you can actually
              do if you were able to inject javascript? There are a lot of uses. Want
              some inspiration?&nbsp;</p>
            <p>Watch this:
              <a href="Watch this: http://www.youtube.com/watch?v=ZCNZJ_7f0Hk"><cite>http://www.youtube.com/watch?v=ZCNZJ_7f0Hk</cite></a> 
            </p>
            <p></p>
            <p>Now for Challenge 2:
              <br> 
            </p>
            <p class="align-left">1. Insert XSS vector into the text box and see what happens when you submit
              it. Sometimes.... developers don't quite secure their applications. Naughty
              naughty!
              <br> 
            </p>
            <p style="" class="pull-left">
              <br> 
            </p>
            <p></p>
            <p></p>
            <a href="/level3" class="btn">Next Challenge</a> 
          </div>
        </div>
      </div>
    </div>
  </body>

</html>"""
