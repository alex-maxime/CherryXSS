# Initial server source code from Jovan Brakus (jovan@brakus.rs) (Many thanks for showing me a great scaffold for CherryPy)
# All levels of the XSS challenge are under the MIT license; Good luck learning!
# Follow me on twitter @infosec_au or take a visit to http://shubh.am
import cherrypy
class l3(object):
    @cherrypy.expose
    def index(self):
      return """<!doctype html>
<html>
  
  <head>
    <title>Level 3</title>
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
            <h1>XSS Challenge&nbsp; 3
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
              <a href="/walkthrough3" class="btn btn-primary btn-large">Walkthrough</a> 
            </p>
            <a href="/level4" class="btn">Next Challenge</a> 
          </div>
        </div>
      </div>
    </div>
  </body>

</html>"""
    @cherrypy.expose
    def name(self, name=None):
      filterlist = ["script","alert","javascript"]
      name = name
      for i in filterlist:
        name = name.replace(i,"")
      return """
            <!doctype html>
<html>
  
  <head>
    <title>Level 3</title>
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
            <h1>XSS Challenge&nbsp; 3
              <br> 
            </h1>
            <p class="align-center">Hi there! I was wondering what your name was. Is your name 1337 h4x0r
              99_I_Hacked_the_Gibson? Woops! Did I get it wrong again? Let me know by entering it down below.
              <br> 
            </p>
<b> HI THERE <a href=\"""" + str(name) + '">' + str(name) + '</a>' + """!</b>
            <p></p>
            <p style="" class="pull-left">
              <br> 
            </p>
            <p></p>
            <p></p>
            <p>
              <a href="/walkthrough3" class="btn btn-primary btn-large">Walkthrough</a> 
            </p>
            <a href="/level4" class="btn">Next Challenge</a> 
          </div>
        </div>
      </div>
    </div>
  </body>

</html>"""
class w3(object):
    @cherrypy.expose
    def index(self):
        return """<!doctype html>
<html>
  
  <head>
    <title>Walkthrough 3</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
    <link rel="stylesheet" href="../static/css/bootstrap.css">
    <link rel="stylesheet" href="../static/css/bootstrap-responsive.css">
    <link rel="stylesheet" href="../static/css/flat-ui.css">
    <script src="../static/js/jquery.min.js"></script>
    <script src="../static/js/bootstrap.min.js"></script>
  </head>
  
  <body>
  <script>
  $(document).ready(function(){
  $("#vectors").hide();
  $("#show").click(function(){
    $("#vectors").fadeIn();
    });
});

</script>
<div class="container">
  <div class="pagination pagination-large pagination-centered">
    <div class="well well-large">
      <div class="hero-unit">
        <h1>Walkthrough&nbsp; 3
          <br> 
        </h1>
        <p class="align-left">Okay. I am assuming you had at least
          <u><b>5</b></u> tries before you came here. Now, hopefully you realised that challenge/level
          3 was the exact same as number 2. The only difference?
          <br> 
        </p>
        <p>The only difference was that the following characters were being filtered
          out: "script", "alert" and "javascript"
          <br> 
        </p>
        <p>Great. Now you know that, do some research and give the challenge a go
          again. If you still are not sure, then click the show vectors button below.
          <br> 
        </p>
        <a class="btn" id="show">Show Vectors</a>
        <a></a>
        <p></p>
        <p style="" class="pull-left">
          <br> 
        </p>
        <p></p>
        <p></p>
        <a href="/level4" class="btn">Next Challenge</a> 
         <div id="vectors">
          <p class="text-error">Possible Vectors
            <br> ================
            <br> The filter is: ["script","alert","javascript"]
            <br> <b> Hmm, try "prompt()" instead of "alert()" </b>
            <br> The filtering does not account for capital letters. Hence: ANY XSS VECTOR
            with those words in capitals will work.
            <br> If you want to be creative, read the following:
            <br>
            <a href="http://incompleteness.me/blog/2008/12/04/xss-filtering/ ">http://incompleteness.me/blog/2008/12/04/xss-filtering/
          </a>
            <br>
            <a href="https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#XSS_Locator ">https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#XSS_Locator
          </a>
            <br> Btw, you should feel a burn if you didn't get this one. Pentesting requires
            you to think outside the box, and sometmes, solutions are very simple workarounds.
            There must've been a thousand ways to get past the filter, but I forgive
            you if you're purely a beginner in web dev or web sec. All the best for the next few
            levels.</p>
        </div>
      </div>
    </div>
  </div>
</div>
  </body>

</html>"""
