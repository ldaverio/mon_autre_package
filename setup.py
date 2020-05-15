"""
Setup mon_autre_package

"""

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md'), encoding='utf-8') as f:
    CHANGES = f.read()

requires = [
    'numpy',
    'mon_package >= 0.2',
]

setup(
    name="mon_autre_package",
    version="0.1",
    packages=find_packages(),
    install_requires=requires,

    # metadata to display on PyPI
    author="Laurent Daverio",
    author_email="laurent.daverio@mines-paristech.fr",
    description="This is the mon_autre_package Package",
    keywords="mon_autre_package example examples",
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
    entry_points="""\
    [console_scripts]
    script_essai = mon_autre_package.scripts.script_essai:main
    """,
)
