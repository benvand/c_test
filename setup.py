"""
test c
"""
from setuptools import setup, find_packages


version = '1.0.0'


setup(
    name='test_c',
    version='1.0.0',
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
