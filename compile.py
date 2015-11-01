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

    qpairs= bottle._parse_qsl(bottle.request.query_string)
    for key, value in qpairs :
        if key == 'args':
            args.append(value)
        
        data = do_command(args, cwd, path )
        
        
        return """<head>
        <script src="/static/js/requirejs/require.js"></script>
        <script src="/default.js"></script>
        <script>display({data});</script>
        </head>
        <body>
        </body>""".format( data=data)
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


    git_submodule(name='js/requirejs',
                  path='static/js/requirejs',
                  url='git@github.com:jrburke/requirejs.git',
                  branch="master")

    grunt(git_submodule(name='js/jquery',
                  path='static/js/jquery',
                  url='git@github.com:jquery/jquery.git',
                  branch="master"))

    git_submodule(name='js/angularjs',
                  path='static/js/angularjs',
                  url='git@github.com:angular/angular.js.git',
                  branch="master")    

    git_submodule(name='js/d3',
                  path='static/js/d3',
                  url='git@github.com:mbostock/d3.git',
                  branch="master")    

    git_submodule(name='js/angular-ui-tree',
                  path='static/js/angular-ui-tree',
                  url='git@github.com:angular-ui-tree/angular-ui-tree.git',
                  branch="master")    

    git_submodule(name='js/angular-ui-grid',
                  path='static/js/angular-ui-grid',
                  url='git@github.com:angular-ui/ui-grid.git',
                  branch="master")

    
    
@route('/default.js')
def default_js():
    return """
    function display(x) {
    
    }
"""
     
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
        
