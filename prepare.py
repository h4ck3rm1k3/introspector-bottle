from html.parser import HTMLParser
import pprint
from html.entities import name2codepoint
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.indent = -1
        self.stack = []
        super().__init__()
        
    def pprint(self, s):
        #if self.indent > 0:
        #print (('  ' * self.indent )  + (s))
        #else:
        #    print(s)
        self.stack[-1]['data'].append(s)
        
    def handle_starttag(self, tag, attrs):
        self.indent = self.indent + 1
        #pprint.pprint(self.stack)
        i = {'name' : tag, 'items':[], 'data' : []}
        self.stack.append(i)
        if attrs:
            #self.pprint("Tag{0}(")
            self.pprint("{1}".format(tag,
                                              ','.join(map( lambda attr : "attr({0})".format(attr) , attrs))))
        #else:
            #self.pprint("Tag{0}(".format(tag))
            
            
    def handle_endtag(self, tag):
        #self.pprint(")")
        self.indent = self.indent -1
        x = self.stack.pop()
        self.stack[-1]['items'].append(x)
                
    def handle_data(self, data):
        if data:
            if re.match("\s+",data):
                pass
            else:
                self.pprint("Data('{0}')".format(data))
                
    def handle_comment(self, data):
        self.pprint("Comment(\"\"\"{0}\"\"\")".format(data))
        
    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        self.pprint("ent('{0}'),".format(c))
        raise Exception()
    
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        self.pprint("Num ent  :", c)
        raise Exception()
    
    def handle_decl(self, data):
        #self.pprint("Decl('{0}'".format(data))
        #raise Exception()
        pass

parser = MyHTMLParser()
import sys
f = open(sys.argv[1])
ls = f.readlines()
for l in ls:
    parser.feed(l)
#pprint.pprint(parser.stack)

def process(x, indent):
    #print (x)
    print (indent + "Tag"+ x['name'] + "(")
    sys.stdout.write(indent + "  ")
    #for d in ):
    s = str("\n"+indent+",")
    print(s.join(x['data']))
    #print (indent + d)
    ci = 0
    for c in x['items']:
        if ci > 0:
            print (indent + "  ,") # add in comma
        ci = ci +1

        process(c,indent + "  ")

    print (indent + ")") 

for x in parser.stack:
    process(x,"")
