# -*- coding: utf-8 -*-
__author__ = 'user'

MTGX_PROPERTY = '{http://maltego.paterva.com/xml/mtgx}Properties/{http://maltego.paterva.com/xml/mtgx}Property'
MTGX_MALTEGO_LINK = '{http://graphml.graphdrawing.org/xmlns}data/{http://maltego.paterva.com/xml/mtgx}MaltegoLink'


class Edge(object):

    def __init__(self, xml_data):
        self.id = xml_data.get('id')
        self.source = xml_data.get('source')
        self.target = xml_data.get('target')
        self.link = xml_data.find(MTGX_MALTEGO_LINK)
        self._link_type = self.link.get('type')
        self.props = {}
        for prop in self.link.findall(MTGX_PROPERTY):
            name = prop.get('name')
            value = prop.find('{http://maltego.paterva.com/xml/mtgx}Value').text or None
            self.props[name] = value

    def link_type(self):
        return self._link_type

    def get_property(self, name):
        if name in self.props:
            return self.props[name]
        else:
            return None

    def __unicode__(self):
        return u'Edge{id: ' + unicode(self.id) + u', source: ' + unicode(self.source) + \
               u', target: ' + unicode(self.target) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')