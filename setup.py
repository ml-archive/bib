import re
import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="Bib",
    version="1.0",
    description="Catching all the spills.",
    long_description="Bib is a module that catches every request to the server and logs them in a palatable manner so that developers can share what they're sending and the response that they get.",
    author="Mai",
    author_email="mnguyen@fuzzproductions.com",
    url="https://github.com/github-user/django-foobar",
    download_url="https://github.com/github-user/django-foobar.git",
    license="MIT License",
    packages=[
        "bib",
    ],
    include_package_data=True,
    install_requires=[
        "Django>=1.7.0",
        "django-bootstrap3>=6.2.2"
    ],
    tests_require=[
        "nose",
        "coverage",
    ],
    zip_safe=False,
    test_suite="tests.runtests.start",
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)