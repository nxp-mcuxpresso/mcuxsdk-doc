from sphinx.writers.latex import LaTeXTranslator
from sphinxmermaid import MermaidNode

def visit_mermaid_node(self, node):
    self.body.append("\n\\begin{verbatim}\n")
    self.body.append(node['code'])  # Include the raw Mermaid code
    self.body.append("\n\\end{verbatim}\n")

def depart_mermaid_node(self, node):
    pass  # No action needed

def preprocess_tables(app, env):
    for docname in env.found_docs:
        doctree = env.get_doctree(docname)
        for node in doctree.traverse():
            if node.tagname == 'table':
                # Check if the table has a tbody element
                tbody_found = False
                for child in node.children:
                    if child.tagname == 'tbody':
                        tbody_found = True
                        break

                if not tbody_found:
                    # Remove the problematic table
                    node.parent.remove(node)

def setup(app):
    app.connect('env-check-consistency', preprocess_tables)
    app.add_node(MermaidNode, latex=(visit_mermaid_node, depart_mermaid_node))
