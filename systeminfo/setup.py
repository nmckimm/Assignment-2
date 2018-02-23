'''
Created on 22 Feb 2018

@author: neil
'''
from setuptools import setup, find_packages

setup(name="systeminfo",
      version="0.1",
      description="Basic system info for COMP30670",
      url="",
      author="Neil McKimm",
      author_email="neil.mckimm@ucdconnect.ie",
      license="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      )
