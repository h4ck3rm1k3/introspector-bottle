# introspector-bottle
The introspector project interface: a python based webserver to manage your programming project and introspect it

# what? another ide?

Yes, this will be a web based, single user, IDE for capturing rich output from commands. It will act as an integration engine for process management of your development process. The library of code will also be usable in batch mode, but the real benefit is for the interactive user interactive mode. We will provide json/rest apis and a javascript front end for customizing the user front end interaction in any way you like.

## collecting of  output files
If you do any code analysis or process analysis you will use multiple tools and soon will have huge amounts of data.
you need a way to collect and organize and parse this data.

## End of monolithic applications

Did you ever wonder why we have these huge isolated monolithic free software applications ? Why is it that everyone has an island of code. As a usr, we need to be able to break down the barriers between modules and see the old main routines as suggestions and documentation of tested use cases. We need the freedom to be able to come up with new paths of execution that meet our needs.

## project management
Be able to bootstrap projects from source based on git. Be able to compile everything from source or use system libs. 

All used files will be 'mounted' like in go into your workspace.  

Support for :
* system libs
* debian packags
* github repos
* maintaining forks of github repos
* other version control systems
* tar.gz management
* extracting patches from urls/mailing lists etc. 
* editing files in emacs and maintaining local patches. 

## smart compilation 
The ultimate goal is to enable smart compilation without huge dependancy nightmares. We want to isolate the exact deps for a given bit of code in the following contexts: 

* deps : what prerequisites do we need 
* configure: how to configure the code
* preprocess : what do we need to do to get the preprocessor to run
* compile : what does it take to compile
* link : how to link it
* load : how to load this
* execute : what is needed to get it to execute (maybe crash)
* coverage : what do we need to do to execute all the code paths
* validate: what is needed to get it to execute validily
* splitting up sources into logical units. we dont need huge files we want small micro units that we can compile and link and load on the fly into a running program.
* dynamic creation of shared objects with code changes or single functions
* wrapping existing shared objects and overloading, intercepting functions
* wrapping object files and compile/link time object interception


Many of these things are hidden in autotools and compiler magic, we need to be able to dive into that at any point.

# plan
Here are some of the tools we want to support :

* strace
* ltrace
* gcc
* binutils
* ldd
* swig
* valgrind
* gdb
