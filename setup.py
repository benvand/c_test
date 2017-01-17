"""
test c
"""
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages


version = '1'


setup(
    name='test_c',
    version='1',
    url='https://github.com/benvand/test_c',
    license='MIT',
    author='benvand',
    description='C',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests'
    ]
)
