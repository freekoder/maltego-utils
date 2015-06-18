from node import Node
from edge import Edge

__author__ = 'user'

ORG_XMLNS_EDGE = '{http://graphml.graphdrawing.org/xmlns}graph/{http://graphml.graphdrawing.org/xmlns}edge'
ORG_XMLNS_NODE = '{http://graphml.graphdrawing.org/xmlns}graph/{http://graphml.graphdrawing.org/xmlns}node'


class Graph(object):

    def __init__(self, xml_data):
        self._edges = []
        self._nodes = []
        for edge in xml_data.findall(ORG_XMLNS_EDGE):
            self._edges.append(Edge(edge))
        for node in xml_data.findall(ORG_XMLNS_NODE):
            self._nodes.append(Node(node))

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges