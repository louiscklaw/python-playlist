# hello.py - http://www.graphviz.org/content/hello

from graphviz import Digraph

g = Digraph('G', filename='/tmp/hello.gv')

g.edge('Hello', 'World')

g.render(format="png")
