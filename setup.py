from setuptools import setup
from setuptools import find_packages

setup(name='rec_gae',
      version='0.1',
      description='Graph Convolutional Matrix Completion',
      author='Rianne van den Berg, Thomas Kipf',
      author_email='riannevdberg@gmail.com',
      url='http://riannevdberg.github.io',
      download_url='https://github.com/riannevdberg/rec_gae',
      license='MIT',
      install_requires=['numpy',
                        'tensorflow',
                        'scipy',
                        'pandas',
                        'cPickle',
                        'h5py'
                        ],
      package_data={'rec_gae': ['README.md']},
      packages=find_packages())