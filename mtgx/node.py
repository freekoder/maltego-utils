from itertools import ifilter

MTGX_VALUE = '{http://maltego.paterva.com/xml/mtgx}Value'
__author__ = 'user'

MTGX_PROPERTY = '{http://maltego.paterva.com/xml/mtgx}Properties/{http://maltego.paterva.com/xml/mtgx}Property'
MTGX_MALTEGO_ENTITY = '{http://graphml.graphdrawing.org/xmlns}data/{http://maltego.paterva.com/xml/mtgx}MaltegoEntity'


class Node(object):

    def __init__(self, graph, xml_data):
        self.graph = graph
        self.id = xml_data.get('id')
        self.entity = xml_data.find(MTGX_MALTEGO_ENTITY)
        self._entity_type = self.entity.get('type')
        self.props = {}
        for prop in self.entity.findall(MTGX_PROPERTY):
            name = prop.get('name')
            value = prop.find(MTGX_VALUE).text or None
            self.props[name] = value

    def entity_type(self):
        return self._entity_type

    def get_property(self, name):
        if name in self.props:
            return self.props[name]
        else:
            return None

    def parents(self):
        pass

    def children(self, node_type=None):
        children_nodes = []
        children_nodes_ids = []
        edges = self.graph.edges(src_node=self)
        for edge in edges:
            target_node = edge.target_node()
            if target_node.id not in children_nodes_ids:
                children_nodes.append(target_node)
                children_nodes_ids.append(target_node.id)
        if node_type:
            children_nodes = ifilter(lambda x: x.entity_type() == node_type, children_nodes)
        return children_nodes

    def parents(self, node_type=None):
        parent_nodes = []
        parent_nodes_ids = []
        edges = self.graph.edges(dst_node=self)
        for edge in edges:
            source_node = edge.source_node()
            if source_node.id not in parent_nodes_ids:
                parent_nodes.append(source_node)
                parent_nodes_ids.append(source_node.id)
        if node_type:
            parent_nodes = ifilter(lambda x: x.entity_type() == node_type, parent_nodes)
        return parent_nodes

    def __unicode__(self):
        return u'Node{id: ' + unicode(self.id) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')