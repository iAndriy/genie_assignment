__author__ = 'aivaney'

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.MD')).read()

requires = [
    'nose==1.3.4',
    'selenium==2.43.0',
    'tornado==4.0.2',
    'coverage==3.7.1',
    'xvfbwrapper==0.2.4',
]


setup(
    name='genie_assignment',
    version='0.0',
    description='genie assignment',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
    ],
    author='Andriy Ivaneyko',
    author_email='aivaney@softserve.com',
    url='https://github.com/iAndriy/genie_assignment.git',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    tests_require=requires,
    zip_safe=True,
    install_requires=requires,
)