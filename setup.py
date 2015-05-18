from setuptools import find_packages
from setuptools import setup

VERSION='0.0.1'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    entry_points={
    },
    include_package_data=True,
    install_requires=[
    ],
    long_description=open('README.rst').read() + '\n' + open('CHANGES.rst').read(),
    name='',
    namespace_packages=[
    ],
    packages=find_packages(),
    version=VERSION,
)
