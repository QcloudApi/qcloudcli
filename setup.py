#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
PACKAGE = 'qcloudcli'
VERSION = __import__(PACKAGE).__version__

def main():
    setup(
        name='qcloudcli',
        version=VERSION,
        description='Universal Command Line Environment for qcloud',
        long_description=open('README.rst').read(),
        author='Qcloud',
        url='https://github.com/QcloudApi/qcloudcli.git',
        maintainer_email="QcloudApi@tencent.com",
        packages = find_packages(),
        platforms=['unix', 'linux', 'win64'],
        scripts = ['qcloudcli/shellcomplete.sh'],
        py_modules=['qcloudcli'],
        entry_points = {
            'console_scripts': [
                'qcloudcli = qcloudcli.Qcloudcli:main',
                'qcloud_completer  = qcloudcli.completer:complete',
            ]
        },
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
    )


if __name__ == '__main__':
    main()
