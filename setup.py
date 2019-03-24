
from setuptools import setup, find_packages
from pz.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='pz',
    version=VERSION,
    description='Simple Package Manager for Developers',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='PyramidZero',
    author_email='contact@pyramidzero.com',
    url='https://github.com/pyramidzero/pzinstaller.git',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'pz': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        pz = pz.main:main
    """,
)
