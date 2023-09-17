from setuptools import setup, find_packages

setup(
    name= 'jsonapi',
    version= '0.0.1',
    install_requires = [],
    package_dir= {"jsonapi": "src"}, 
    packages= find_packages(
        where= 'src',
        include= ['jsonapi'],
    ),

    extras_require = {
        "test": ["pytest"]
    },

    python_requires = ">= 3.6"
    )