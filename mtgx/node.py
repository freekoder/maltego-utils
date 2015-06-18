MTGX_VALUE = '{http://maltego.paterva.com/xml/mtgx}Value'
__author__ = 'user'

MTGX_PROPERTY = '{http://maltego.paterva.com/xml/mtgx}Properties/{http://maltego.paterva.com/xml/mtgx}Property'
MTGX_MALTEGO_ENTITY = '{http://graphml.graphdrawing.org/xmlns}data/{http://maltego.paterva.com/xml/mtgx}MaltegoEntity'


class Node(object):

    def __init__(self, xml_data):
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

    def __unicode__(self):
        return u'Node{id: ' + unicode(self.id) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')