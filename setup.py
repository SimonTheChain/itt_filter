from distutils.core import setup
import py2exe

setup(windows=[{"script" : "itt_filter.py"}], 
options={"py2exe" : {"includes" : ["docx", 'lxml.etree', 'lxml._elementpath', 'gzip', "sip", "PyQt4"]}})
