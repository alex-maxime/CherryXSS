# Initial server source code from Jovan Brakus (jovan@brakus.rs) (Many thanks for showing me a great scaffold for CherryPy)
# All levels of the XSS challenge are under the MIT license; Good luck learning!
# Follow me on twitter @infosec_au or take a visit to http://shubh.am
import cherrypy
import cgi
class l4(object):
    @cherrypy.expose
    def index(self):
      return """<!doctype html>
<html>
  
  <head>
    <title>Level 4</title>
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
        <h1>XSS Challenge&nbsp; 4
          <br> 
        </h1>
        <p class="align-center">*cough* This page uses cgi.escape. Any known bypasses? Insert the path
          of an image that you want displayed below. This image will be shown between
          img tags.
          <br> 
        </p>
 <form action="imagelink" method="get">
          <input placeholder="erhmerhgerhd img path" name="imagelink" class="input-large"
          type="text">
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
          <a href="/walkthrough4" class="btn btn-primary btn-large">Walkthrough</a> 
        </p>
        <a href="/level5" class="btn">Next Challenge</a> 
      </div>
    </div>
  </div>
</div>
  </body>

</html>"""
    @cherrypy.expose
    def imagelink(self, imagelink=None):
      filterlist = ["script","javascript", "alert"]
      imagelink = cgi.escape(imagelink)
      for i in filterlist:
        imagelink = imagelink.replace(i,"")
      return """
            <!doctype html>
<html>
  
  <head>
    <title>Level 4</title>
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
        <h1>XSS Challenge&nbsp; 4
          <br> 
        </h1>
        <p class="align-center">*cough* This page uses cgi.escape. Any known bypasses? Insert the path
          of an image that you want displayed below. This image will be shown between
          img tags.
          <br> 
        </p>
        <form action="imagelink">
          <input placeholder="erhmerhgerhd img path" name="imagelink" class="input-large"
          type="text">
          <div class="form-actions">
            <button type="submit" class="btn btn-primary">Submit</button>
            <input class="btn" value="Reset" type="reset"> 
          </div>
        </form>
<br><p><img src=\"""" + str(imagelink) + "\">" + """Image above mate</p>
            <p></p>
            <p style="" class="pull-left">
              <br> 
            </p>
            <p></p>
            <p></p>
            <p>
              <a href="/walkthrough4" class="btn btn-primary btn-large">Walkthrough</a> 
            </p>
            <a href="/level5" class="btn">Next Challenge</a> 
          </div>
        </div>
      </div>
    </div>
  </body>

</html>"""
class w4(object):
    @cherrypy.expose
    def index(self):
        return """<!doctype html>
<html>
  
  <head>
    <title>Walkthrough 4</title>
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
        <h1>Walkthrough&nbsp; 4
          <br> 
        </h1>
        <p class="align-center">Well done for getting to level 4. Now, no worries if you didn't get this
          one, it was kind of tricky.
          <br> 
        </p>
        <p>It's important to not what cgi.escape does. Here is a little demonstration
          of it's use taken from xssed.me
          <br> 
        </p>
<!-- HTML generated using hilite.me --><div style="background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><table><tr><td><pre style="margin: 0; line-height: 125%">1
2
3
4
5
6
7
8
9</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #666666">~&gt;</span> python
Python <span style="color: #666666">2.3.5</span> (<span style="color: #008800; font-style: italic">#2, Aug 30 2005, 15:50:26) </span>
Type <span style="color: #BB4444">&quot;help&quot;</span>, <span style="color: #BB4444">&quot;copyright&quot;</span>, <span style="color: #BB4444">&quot;credits&quot;</span> <span style="color: #AA22FF; font-weight: bold">or</span> <span style="color: #BB4444">&quot;license&quot;</span> <span style="color: #AA22FF; font-weight: bold">for</span> more information<span style="color: #666666">.</span>
<span style="color: #666666">&gt;&gt;&gt;</span> <span style="color: #AA22FF; font-weight: bold">import</span> <span style="color: #0000FF; font-weight: bold">cgi</span>
<span style="color: #666666">&gt;&gt;&gt;</span> <span style="color: #AA22FF; font-weight: bold">print</span> <span style="color: #BB4444">&quot;&lt;script&gt;alert(&#39;xss&#39;);&lt;/script&gt;&quot;</span>
<span style="color: #666666">&lt;</span>script<span style="color: #666666">&gt;</span>alert(<span style="color: #BB4444">&#39;xss&#39;</span>);<span style="color: #666666">&lt;/</span>script<span style="color: #666666">&gt;</span>

<span style="color: #666666">&gt;&gt;&gt;</span> <span style="color: #AA22FF; font-weight: bold">print</span> cgi<span style="color: #666666">.</span>escape(<span style="color: #BB4444">&quot;&lt;script&gt;alert(&#39;xss&#39;);&lt;/script&gt;&quot;</span>);
<span style="color: #666666">&amp;</span>lt;script<span style="color: #666666">&amp;</span>gt;alert(<span style="color: #BB4444">&#39;xss&#39;</span>);<span style="color: #666666">&amp;</span>lt;<span style="color: #666666">/</span>script<span style="color: #666666">&amp;</span>gt;
</pre></td></tr></table></div>

        <p>Anyways, read the following and if you still don't understand what to
          do, feel free to click the "Show Vectors" button. Good luck.
          <br> 
        </p>
        <p>Final tip: This level has the filter from level 3, except it ALSO uses
          cgi.escape. Look into possible events you can trigger ;) *cough* onmouseover
          <br> 
        </p>
        <p></p>
        <p></p>
        <a id="show" class="btn">Show Vectors</a>
        <a></a>
        <p></p>
        <p style="" class="pull-left">
          <br> 
        </p>
        <p></p>
        <p></p>
        <a href="/level5" class="btn">Next Challenge</a>
        <div id="vectors">
          <p class="text-error">Possible Vectors
            <br> ================
            <br> The filter is: ["script","alert","javascript"] + cgi.escape()
            <br> For this challenge, realise that user input is being inserted into an
            img field and hence the following vectors can be used:
            <br> x" onerror=prompt(1)//
            <br> 
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
  </body>

</html>"""
