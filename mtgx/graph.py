from itertools import ifilter
from node import Node
from edge import Edge

__author__ = 'user'

ORG_XMLNS_EDGE = '{http://graphml.graphdrawing.org/xmlns}graph/{http://graphml.graphdrawing.org/xmlns}edge'
ORG_XMLNS_NODE = '{http://graphml.graphdrawing.org/xmlns}graph/{http://graphml.graphdrawing.org/xmlns}node'


class Graph(object):

    def __init__(self, xml_data):
        self._id_node_map = {}
        self._edges = []
        self._nodes = []
        for edge in xml_data.findall(ORG_XMLNS_EDGE):
            self._edges.append(Edge(self, edge))
        for node in xml_data.findall(ORG_XMLNS_NODE):
            node_elem = Node(self, node)
            self._nodes.append(node_elem)
            self._id_node_map[node_elem.id] = node_elem

    def nodes(self, type=None):
        _nodes = self._nodes
        if type:
            _nodes = ifilter(lambda x: x.entity_type() == type, _nodes)
        return _nodes

    def get_node_by_id(self, node_id):
        if node_id in self._id_node_map:
            return self._id_node_map[node_id]
        else:
            return None

    def node_present(self, node):
        for graph_node in self._nodes:
            if node.id == graph_node.id:
                return True
        return False

    def edges(self, src_node=None, dst_node=None):
        _edges = self._edges
        if src_node:
            _edges = ifilter(lambda x: x.source == src_node.id, _edges)
        if dst_node:
            _edges = ifilter(lambda x: x.target == dst_node.id, _edges)
        return _edges