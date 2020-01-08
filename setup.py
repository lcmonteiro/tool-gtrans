# #################################################################################################
# -------------------------------------------------------------------------------------------------
# File:   setup.py
# Author: Luis Monteiro
#
# Created on jan 6, 2020, 22:00 PM
# -------------------------------------------------------------------------------------------------
# #################################################################################################
from setuptools import setup, find_packages

# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------
with open('README.md', 'r') as fh:
    long_description = fh.read()

# -----------------------------------------------------------------------------
# setup
# -----------------------------------------------------------------------------
setup(
    name='gtranslate',
    version='0.1',
    description='Free Google Translate API service',
    long_description=long_description,
    keywords='google translate api free python gtranslate',
    url='https://github.com/lcmonteiro/tool-gtranslate',
    author='Luis Monteiro',
    author_email='monteiro.lcm@gmail.com',
    license='MIT',  
    classifiers=[
        'License :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
    packages=[
        'gtranslate',
        'gtranslate.providers'
    ],
    package_data={
        'gtranslate.providers': ['uagents.txt']
    },
    install_requires=[
         'selenium',
         'googletrans',
         'chromedriver-binary==79.0.3945.36.0'
    ]
)
# #################################################################################################
# -------------------------------------------------------------------------------------------------
# end
# -------------------------------------------------------------------------------------------------
###################################################################################################
