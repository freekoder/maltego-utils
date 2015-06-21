__author__ = 'user'

from setuptools import setup, find_packages

setup(name='mtgx',
      version='0.1',
      description='maltego project graph walker',
      author='Alexander Rudakov',
      author_email='freekoder@yandex.ru',
      url='https://github.com/freekoder/maltego-utils',
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          ],
      keywords='maltego graph',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'examples'])
      )
