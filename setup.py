from setuptools import setup, find_packages

from version import version

setup(
    name='EPFImporter',
    version=version,
    packages=find_packages(),
    long_description='A Python CLI tool for importing Apple Enterprise Partner Feed data, '
                     'available to EPF partners, into a relational database.',
    install_requires=[
        'pymysql==0.10.1',
        'psycopg2==2.7.4',
    ],
)
