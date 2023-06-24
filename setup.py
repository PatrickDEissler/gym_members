from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gym_members/__init__.py
from gym_members import __version__ as version

setup(
	name="gym_members",
	version=version,
	description="App for the Frappe Developer\'s Certification (Final Assignment)",
	author="Patrick Eissler (ALYF GmbH)",
	author_email="patrick@alyf.de",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
