from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in general/__init__.py
from general import __version__ as version

setup(
	name="general",
	version=version,
	description="All Apps for Businesses",
	author="kunleadenuga",
	author_email="kunleadenuga@live.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
