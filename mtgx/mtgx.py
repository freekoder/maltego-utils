from zipfile import ZipFile
from xml.etree.cElementTree import XML
from graph import Graph

__author__ = 'user'


class MTGX(object):

    def __init__(self, filename):
        zipfile = ZipFile(filename)
        if u'Graphs/Graph1.graphml' not in zipfile.namelist():
            raise RuntimeError('maltego mtgx-file has no any graph data')
        xml = XML(zipfile.open(u'Graphs/Graph1.graphml').read())
        self._graph = Graph(xml)

    def graph(self):
        return self._graph