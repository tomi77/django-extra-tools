from setuptools import setup


setup(
    name="t77-django",
    version='0.1',
    author="Tomasz Jakub Rup",
    author_email="tomasz.rup@gmail.com",
    url='https://github.com/tomi77/python-t77-django',
    description='A set of functions related with Django',
    long_description=open("README.md").read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    license='MIT',
    install_requires=['Django >= 1.4.3'],
    packages=['t77_django']
)
