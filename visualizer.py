import pydot

def _build_pydot_tree(node, graph, parent_id=None):
    """Node nesnesini recursive olarak gezer ve pydot grafiği oluşturur."""
    if not node:
        return
    
  
    current_id = str(id(node))
    
    
    label = f'"{node.name}"'
    if node.value:
        label = f'"{node.name}\\n({node.value})"'
    
  
    pydot_node = pydot.Node(current_id, label=label, shape="ellipse", fontname="Arial")
    graph.add_node(pydot_node)
    
   
    if parent_id:
        edge = pydot.Edge(parent_id, current_id)
        graph.add_edge(edge)
    
   
    for child in node.children:
        _build_pydot_tree(child, graph, current_id)

def create_parse_tree_png(root_node, filename="parse_tree.png"):
    """
    Verilen kök düğümden (Node) bir PNG dosyası üretir.
    """
    
    graph = pydot.Dot("parse_tree", graph_type="digraph", rankdir="TB")
    
    
    _build_pydot_tree(root_node, graph)
    
   
    try:
        graph.write_png(filename)
        print(f" -> Görsel başarıyla oluşturuldu: {filename}")
    except Exception as e:
        print(f" -> HATA: Görsel oluşturulamadı. Sistemde Graphviz kurulu mu? \nDetay: {e}")