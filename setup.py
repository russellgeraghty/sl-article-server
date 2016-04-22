import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "Article Server",
    version = "0.0.1",
    author = "Russell Geraghty",
    author_email = "russell@rosesareblue.co.uk",
    description = "A simple article server.",
    license = "Apache 2.0",
    keywords = "news article server",
    url = "https://github.com/russellgeraghty/sl-article-server.git",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2 License",
    ],
    entry_points = {
        'console_scripts': ['article-server=server.rest_server:main'],
    }

)
