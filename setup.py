# -*- coding: utf-8 -*-

import io
import ast
from re import compile
from setuptools import setup


def _get_version():
    version_re = compile(r'__version__\s+=\s+(.*)')

    with open('up2cos.py', 'rb') as fh:
        version = ast.literal_eval(version_re.search(
            fh.read().decode('utf-8')).group(1))

    return str(version)


def _get_author():
    author_re = compile(r'__author__\s+=\s+(.*)')
    mail_re = compile(r'(.*)\s<(.*)>')

    with open('up2cos.py', 'rb') as fh:
        author = ast.literal_eval(
            author_re.search(fh.read().decode('utf-8')).group(1)
        )
    mail = mail_re.search(author)
    return (mail.group(1), mail.group(2)) if mail else (author, None)


def _get_readme():
    with io.open('README.rst', 'rt', encoding='utf8') as f:
        return f.read()


version = _get_version()
(author, email) = _get_author()
setup(
    name='up2cos',
    version=version,
    license='BSD 3-Clause',
    author=author,
    author_email=email,
    description='Save uploaded pictures in Tencent COS.',
    long_description=_get_readme(),
    url='https://github.com/staugur/picbed-up2cos',
    py_modules=['up2cos', ],
    zip_safe=False,
    install_requires=['cos-python-sdk-v5>1.6.0']
)
