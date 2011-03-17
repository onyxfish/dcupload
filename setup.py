#!/usr/bin/env python

from distutils.core import setup

setup(name='dcupload',
    version='0.0.1',
    description='Bulk upload utility for DocumentCloud.',
    author='Christopher Groskopf',
    author_email='staringmonkey@gmail.com',
    url='https://github.com/onyxfish/dcupload',
    license='MIT',
    py_modules = ['MultipartPostHandler'],
    scripts = ['dcupload'],
    )
