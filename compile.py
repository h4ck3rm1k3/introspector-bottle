#!/usr/bin/python3.4
from bottle import route, run, template, request
import bottle
import json
import sys
import subprocess
import os
#from urlparse import urlparse

from bottle import static_file

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

sys.path.append('workspace/py/path.py')
from path import Path

def do_command(args, path ):
    d = Path('workspace')
    if path :
        d = d /  path
    print ("going into {0}".format(d))
    if (not d.exists()):
        raise Exception(d3)
    
    p = subprocess.Popen(args,
                         shell=True, 
                         #stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         cwd=d)
    stdout = p.stdout
    stderr = p.stderr
    stdout_o = stdout.read().decode("utf-8").split("\n") #.read()
    stderr_o = stderr.read().decode("utf-8").split("\n")
    retcode = p.wait();
    data = json.dumps({
        'path' : d,
        'stdout': stdout_o,
        'stderr': stderr_o,
        'cmd' : args,
        'retcode' : retcode,
    })        
        
    print (data)
    if not retcode == 0:
        raise Exception("bad return")
    return data
    
# cmd is array of args
@route('/run/<cwd>/<cmd>')
def run_command(cmd, cwd):
    d = Path('workspace')
    args = [cmd]
    path = bottle.request.params.get('path')
    if path :
        cwd = cwd /  path
    qpairs= bottle._parse_qsl(bottle.request.query_string)
    for key, value in qpairs :
        if key == 'args':
            args.append(value)
        
        data = do_command(args, cwd )
        
        
        return """<html>
<head>
  <!-- bower:css -->
  <link rel="stylesheet" href="/static/js/bootstrap/dist/css/bootstrap.css" />
  <link rel="stylesheet" href="/static/js/angular-ui-tree/dist/angular-ui-tree.min.css" />

  <!-- uigrid -->
  <link rel="stylesheet" href="/static/js/angular-ui-grid/ui-grid.css" />
  
  <link rel="stylesheet" href="/static/js/animate.css/animate.css" />
  <link rel="stylesheet" href="/static/js/fontawesome/css/font-awesome.css" />

  <link rel="stylesheet" href="/static/css/introspector.css" />
 
  <!-- endbower -->
        </head>
        <body ng-app="introspectorApp">
        <!-- bower:js -->
        <script src="/static/js/jquery/dist/jquery.js"></script>
        <script src="/static/js/angular/angular.js"></script>
        <script src="/static/js/bootstrap/dist/js/bootstrap.js"></script>
        <script src="/static/js/angular-animate/angular-animate.js"></script>
        <script src="/static/js/angular-aria/angular-aria.js"></script>
        <script src="/static/js/angular-cookies/angular-cookies.js"></script>
        <script src="/static/js/angular-messages/angular-messages.js"></script>
        <script src="/static/js/angular-resource/angular-resource.js"></script>
        <script src="/static/js/angular-route/angular-route.js"></script>
        <script src="/static/js/angular-sanitize/angular-sanitize.js"></script>
        <script src="/static/js/angular-touch/angular-touch.js"></script>
        <script src="/static/js/angular-bootstrap/ui-bootstrap-tpls.js"></script>
        <script src="/static/js/angular-ui-tree/dist/angular-ui-tree.js"></script>
        <script src="/static/js/angular-ui-grid/ui-grid.js"></script>
        <script src="/static/js/d3/d3.js"></script>

        <!-- v1 -->
        <link rel="stylesheet" href="/static/js/angular-json-edit/dist/styles/jsonEditor.css">
        <script src="/static/js/angular-json-edit/dist/angularJsonEdit.js"></script>
        

        <!-- editor -->
        <script type="text/javascript" src="/static/js/ace-builds/src-min-noconflict/ace.js"></script>
        <script type="text/javascript" src="/static/js/angular-ui-ace/ui-ace.js"></script>
        
        <!-- endbower -->
        <script src="/static/js/introspector/default.js"></script>


        <!-- warning large data object injected here! -->
        <div id=raw-data-object class=raw-data data-ng-init='raw_data_object={data}'></div>

<!-- Add your site or application content here -->
    <div class="header">
      <div class="navbar navbar-default" role="navigation">
        <div class="container">
          <div class="navbar-header">

            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#js-navbar-collapse">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>

            <a class="navbar-brand" href="#/">introspector</a>
          </div>

          <div class="collapse navbar-collapse" id="js-navbar-collapse">

            <ul class="nav navbar-nav">
              <li class="active"><a href="#/">Home</a></li>

              <li><a ng-href="#/tree">Tree</a></li>
              <li><a ng-href="#/graph">Graph</a></li>
              <li><a ng-href="#/table">Table</a></li>
              <li><a ng-href="#/source">Source</a></li>

              <li><a ng-href="#/about">About</a></li>

            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
    <div ng-view=""></div>
    </div>

    <div class="footer">
      <div class="container">
        <p>made by the Introspector Team</p>
      </div>
    </div>


    <script src="/static/js/introspector/app.js"></script>
    <script src="/static/js/introspector/controllers/main.js"></script>
    <script src="/static/js/introspector/controllers/about.js"></script>
    <script src="/static/js/introspector/controllers/tree.js"></script>
    <script src="/static/js/introspector/controllers/table.js"></script>
    <script src="/static/js/introspector/controllers/graph.js"></script>
    <script src="/static/js/introspector/controllers/source.js"></script>
        


        </body>
        </html>""".format( data=data)
    else:
        return template('<b>dir does not exists {{d3}}</b>!', d3=d3)

#import pygit2
#from git.objects.submodule.base import Submodule

# create a new venv
def python_create_venv ():
    pass

def python_install_venv ():
    # install this module into venv
    pass
    
# add a git submodule into the project
def git_submodule(name, path, url, branch):
    #print sys.path
    from git.repo.base import Repo
    d = str(Path('.').abspath())
    repo = Repo(d)  # current repo

    from git.objects.submodule.base import Submodule
    s = Submodule.add(repo,name,path, url, branch)
    
    #s = self.repo.lookup_submodule(SUBM_PATH)
    #self.repo.listall_submodules()

    return str(Path(path).abspath())

# one time setup to install all prerequisites


# requires GitPython to be installed: https://github.com/gitpython-developers/GitPython

# remote_url = Repo().remotes.origin.url
# parsed = urlparse(remote_url)
# remote_path = parsed.path
# if parsed.netloc:
#     remote_host = parsed.netloc
# else:
#     remote_host = parsed.scheme
def grunt (p):
    print ("running grunt in", p)
    do_command('npm install',p)
    do_command('npm install grunt',p)
    do_command('grunt',p)
    
def git_my_submodule_python(source_dir=None, mount=None, original=None, my_repo=None):

    if not mount:
        raise Exception("no mount")
    
    if source_dir:
        p = do_mount(source_dir, mount)
    else:
        p = workspace_dir(mount)
        
    if p not in sys.path:
        sys.path.append(p)
    return p
    # update submodules for that module
    

def run_pip(req):
    import pip
    pip.main(initial_args = ['install', "-e", req ])
    
@route('/setup')
def requirements() :
    #run_pip(
    #    'git+ssh://git@github.com:gitpython-developers/gitdb.git#egg=gitdb'
    #)


    
    git_my_submodule_python(
                     mount='py/path.py',
                     original='git@github.com:jaraco/path.py.git',
                     my_repo='git@github.com:h4ck3rm1k3/path.py.git')


    git_my_submodule_python(source_dir='../../GitPython',
                     mount='py/gitpython',
                     original='git@github.com:gitpython-developers/GitPython.git',
                     my_repo='git@github.com:h4ck3rm1k3/GitPython.git')


    # git_submodule(name='js/requirejs',
    #               path='static/js/requirejs',
    #               url='git@github.com:jrburke/requirejs.git',
    #               branch="master")

    # grunt(git_submodule(name='js/jquery',
    #               path='static/js/jquery',
    #               url='git@github.com:jquery/jquery.git',
    #               branch="master"))

    # bower(git_submodule(name='js/angularjs',
    #               path='static/js/angularjs',
    #               url='git@github.com:angular/angular.js.git',
    #               branch="master"))

    # git_submodule(name='js/d3',
    #               path='static/js/d3',
    #               url='git@github.com:mbostock/d3.git',
    #               branch="master")    

    # git_submodule(name='js/angular-ui-tree',
    #               path='static/js/angular-ui-tree',
    #               url='git@github.com:angular-ui-tree/angular-ui-tree.git',
    #               branch="master")    

    # git_submodule(name='js/angular-ui-grid',
    #               path='static/js/angular-ui-grid',
    #               url='git@github.com:angular-ui/ui-grid.git',
    #               branch="master")
    
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/clone/<url>')
def clone(name):
    return template('<b>going to clone {{url}}</b>!', name=name)

def workspace_dir(name):
    d = Path('workspace')
    if (not d.exists()):
        d.mkdir()
    d3 = d / name
    if (not d3.parent.exists()):
        d3.parent.mkdir()
    return d3.abspath()

def do_mount(path, name):
    d3 = workspace_dir(name)
    d2 = Path(path).abspath()
    if (not d3.exists()):
        if d2.exists():
            d2.symlink(d3)
    return d3

@route('/mount/<name>')
def mount(name):
    path = bottle.request.params.get('path')
    do_mount(path, name)
    return template('<b>going to mount {{name}}</b> {{path}}!',
                    name=name,
                    path=path)

def test():
    do_mount("/tmp", "test")

requirements()

run(host='localhost',
    port=8080,
    debug=True, 
    reloader=True,
    reload_interval=1
)
        
