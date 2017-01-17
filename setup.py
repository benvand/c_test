"""
test c
"""
from setuptools import setup, find_packages


version = '1.0.0'


setup(
    name='c_test',
    version='1.0.0',
    url='https://github.com/benvand/c_test',
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
