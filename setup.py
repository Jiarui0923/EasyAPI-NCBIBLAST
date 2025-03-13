from setuptools import setup, find_packages
import os


LONG_DESCRIPTION = '''
This project build RESTful-API based on EasyAPI for BLAST use remote NCBI server.

If there is any issue, please put up with an issue or contact Jiarui Li (jli78@tulane.edu)
'''
VERSION = '0.0.1'
NAME = 'EasyAPI-NCBIBLAST'


install_requires = [
    "easyapi",
    "requests",
]


setup(
    name=NAME,
    description="NCBI BLAST for EasyAPI.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    version=VERSION,
    packages=find_packages(),
    install_requires=install_requires,
    url="https://git.tulane.edu/apl/computeservices/easyapi-extentions/easy-api-ncbiblast",
    author="Jiarui Li, Marco K. Carbullido, Jai Bansal, Samuel J. Landry, Ramgopal R. Mettu",
    author_email=("jli78@tulane.edu"),
    maintainer=("Jiarui Li"),
    maintainer_email="jli78@tulane.edu",
    license="GPLv3",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GPLv3 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Build Tools",
    ],
    zip_safe=True,
    platforms=["any"],
)
