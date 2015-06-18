#!/usr/bin/env python
__author__ = 'user'

import mtgx


def main():
    project = mtgx.MTGX('/home/user/MaltegoProjects/sample.mtgx')
    for node in project.graph().nodes(type='maltego.Domain'):
        print node.get_property('fqdn')
        for child in node.children():
            print (u'\t' + unicode(child))

if __name__ == '__main__':
    main()
