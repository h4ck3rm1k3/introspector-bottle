# introspector-bottle
The introspector project interface: a python based webserver to manage your programming project and introspect it

# what? another ide?

Yes, this will be a web based, single user, IDE for capturing rich output from commands. 

## collecting of  output files
If you do any code analysis or process analysis you will use multiple tools and soon will have huge amounts of data.
you need a way to collect and organize and parse this data.

## project management
Be able to bootstrap projects from source based on git. Be able to compile everything from source or use system libs. 
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
