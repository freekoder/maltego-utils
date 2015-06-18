#!/usr/bin/env python
__author__ = 'user'

import mtgx


def main():
    project = mtgx.MTGX('/home/user/MaltegoProjects/sample.mtgx')
    for edge in project.graph().edges():
        print edge.link_type()

if __name__ == '__main__':
    main()
