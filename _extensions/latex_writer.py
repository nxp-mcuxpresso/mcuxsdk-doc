from sphinx.writers.latex import LaTeXTranslator
from sphinxmermaid import MermaidNode

def visit_mermaid_node(self, node):
    self.body.append("\n\\begin{verbatim}\n")
    self.body.append(node['code'])  # Include the raw Mermaid code
    self.body.append("\n\\end{verbatim}\n")

def depart_mermaid_node(self, node):
    pass  # No action needed

def setup(app):
    app.add_node(MermaidNode, latex=(visit_mermaid_node, depart_mermaid_node))
