"""
test c
"""
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages


requirements = list(parse_requirements('requirements.txt',
                                       session=pip.download.PipSession()))

install_requires = [str(r.req) for r in requirements]

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
    install_requires=install_requires
)
