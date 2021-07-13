from setuptools import setup, Extension, find_packages
import sys

__author__ = "etseng@pacb.com"
version = "v1.0.0"

setup(
    name = 'magphase',
    version=version,
    author='Elizabeth Tseng',
    author_email='etseng@pacb.com',
    zip_safe=False,
    packages = ['phasing.io'],

    install_requires=[
        'biopython',
        'bx-python>=0.7.3',
        'scipy',
        'pysam'
        ],
    scripts = [
			   'phasing/mag_phaser.py',
               'phasing/utils/paint_bam_post_phaser.py'
               ],
    )
