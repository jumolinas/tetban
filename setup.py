
from setuptools import setup, find_packages
from tetban.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='tetban',
    version=VERSION,
    description='Apply rules in tetration from command line',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Julio Molina Soler',
    author_email='jmolinas@cisco.com',
    url='https://github.com/jumolinas/tetban',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'tetban': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        tetban = tetban.main:main
    """,
)
