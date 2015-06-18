#!/usr/bin/env python
__author__ = 'user'

import mtgx


def main():
    project = mtgx.MTGX('/home/user/MaltegoProjects/sample.mtgx')
    for node in project.graph().nodes():
        print node.entity_type()

if __name__ == '__main__':
    main()
