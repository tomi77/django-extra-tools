from setuptools import setup, find_packages

from django_extras import __version__, __author__, __email__, __license__


setup(
    name="django_extras",
    version=__version__,
    author=__author__,
    author_email=__email__,
    url='https://github.com/tomi77/django_extras',
    description='A set of functions related with Django',
    long_description=open("README.rst").read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: PL/SQL',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    license=__license__,
    install_requires=['Django >= 1.4.3'],
    packages=find_packages(exclude=['tests']),
    package_data={
        'django_extras': ['sql/*.sql'],
    }
)
