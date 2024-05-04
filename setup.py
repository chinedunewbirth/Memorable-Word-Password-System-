#import library for building wheels
from setuptools import setup, find_packages
    
setup(
    name='memo_pass',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography',  # Add any other dependencies here
    ],
    author='Chinedu Mazi',
    author_email='chinedumazigtv@gmail.com',
    description='memorable password',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8.18',
    ],
)
