try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import http_dumper

required = [
    'bottle',
]

packages = [
    'http_dumper',
]

scripts = [
    'bin/http_dumper',
]

setup(
    name='http_dumper',
    version=http_dumper.__version__,
    description='HTTP Dumper',
    long_description=open('README.rst').read(),
    author='Greg Taylor',
    author_email='gtaylor@gc-taylor.com',
    url='https://github.com/gtaylor/http_dumper',
    packages=packages,
    scripts=scripts,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=required,
    license='BSD',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)