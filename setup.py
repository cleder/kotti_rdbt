from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='kotti_rdbt',
      version=version,
      description="Kotti RDB Tables",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Christian Ledermann',
      author_email='christian.ledermann@gmail.com',
      url='https://github.com/cleder/',
      license='BSD-derived',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'Kotti',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )