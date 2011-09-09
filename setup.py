from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='chatter',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='bischjer',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=[
          # -*- Extra requirements: -*-
        'twisted',
        'unittest2',
        'Mock>=0.7',
        'Fabric==1.1.0',
      ],
      entry_points={
        'console_scripts': [
            'chatterd = chatter.server.Server:start',
            'chatter = chatter.frontend.app:start',
            ],
        },
      )
