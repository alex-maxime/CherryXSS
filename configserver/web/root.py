import cherrypy
class indexserver(object):
	@cherrypy.expose
	def index(self):
		return """
		<!doctype html>
<html>
  
  <head>
    <title>Welcome</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
    <link rel="stylesheet" href="../static/css/bootstrap.css">
    <link rel="stylesheet" href="../static/css/bootstrap-responsive.css">
    <link rel="stylesheet" href="../static/css/flat-ui.css">
    <script src="../static/js/jquery.min.js"></script>
    <script src="../static/js/bootstrap.min.js"></script>
  </head>
  
  <body>
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="#">CherryXSS: Cross Site Scripting Playground</a>
          <div class="navbar-content">
            <ul class="nav  pull-right">
              <li class="active">
                <a href="#">Intro</a> 
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="page-header">
        <h1>Welcome!</h1>
      </div>
      <p class="lead">CherryXSS is an open source cross site scripting playground, where hackers
        can code their own challenges for others to try out. XSS is commonly increasing
        and while proper programming practice is also developing - cross site scripting
        remains one of the most common web vulnerabilities around.
        <br> 
      </p>
      <p>Give the levels down below a go, if you need help, feel free to go through
        their respective walkthroughs or contact me at
        <a href="https://twitter.com/infosec_au">@infosec_au</a> or
        <a href="http://shubh.am">shubh.am</a>
        <br> 
      </p>
      <div class="row">
        <div class="span4">
          <div class="well">
            <h4>Level 1
              <br> 
            </h4>
            <a href="/level1" class="btn pull-left btn-primary">Start!</a>
            <br>
            <br>
            <a href="/level1" class="btn pull-left">Walkthrough</a>
            <div>
              <br> 
            </div>
            <p></p>
          </div>
          <div class="well">
            <h4>Level 4
              <br> 
            </h4>
            <a href="/level1" class="btn pull-left btn-primary">Start!</a>
            <br>
            <br>
            <a href="/level1" class="btn pull-left">Walkthrough</a>
            <div>
              <br> 
            </div>
          </div>
        </div>
        <div class="span4">
          <div class="well">
            <h4>Level 2
              <br> 
            </h4>
            <a href="/level1" class="btn pull-left btn-primary">Start!</a>
            <br>
            <br>
            <a href="/level1" class="btn pull-left">Walkthrough</a>
            <div>
              <br> 
            </div>
          </div>
          <div class="well">
            <h4>Level 5
              <br> 
            </h4>
            <p>Under Construction
              <br> 
            </p>
          </div>
        </div>
        <div class="span4">
          <div class="well">
            <h4>Level 3
              <br> 
            </h4>
            <a href="/level1" class="btn pull-left btn-primary">Start!</a>
            <br>
            <br>
            <a href="/level1" class="btn pull-left">Walkthrough</a>
            <div>
              <br> 
            </div>
          </div>
          <div class="well">
            <h4>Level 6
              <br> 
            </h4>
            <p>Under Construction
              <br> 
            </p>
          </div>
        </div>
      </div>
      <p class="text-info lead">Enjoy. Hope you learn something.
        <br> 
      </p>
    </div>
  </body>

</html>"""