from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in business_theme_v14/__init__.py
from theme_v15 import __version__ as version

setup(
	name="theme_v15",
	version=version,
	description=" Theme for ERPNext / Frappe",
	author="Mszenma",
	author_email="szenma@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
