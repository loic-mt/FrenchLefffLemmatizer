import sys
from setuptools import setup, find_packages

setup(
   name = "FrenchLefffLemmatizer",
   version = "?",
   description = "Lemmatize French words",
   author = "Claude Coulombe",
   author_email = "claude.coulombe@gmail.com",
   url='https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer',
   classifiers=[
       'Development Status :: ?',
       'Intended Audience :: ?',
       'License :: Apache License, Version 2.0',
       'Programming Language :: Python',
       'Programming Language :: Python :: 3',
     ],
    entry_points="""
    """,
   license='Apache License, Version 2.0',
   packages=find_packages(),
   py_modules=['FrenchLefffLemmatizer'],
   include_package_data=True,
   zip_safe=False,
)
