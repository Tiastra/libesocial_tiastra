import os
import re
from setuptools import find_packages, setup

from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    'requests>=2.26.0',
    'lxml>=4.6.3',
    'zeep>=4.1.0',
    'signxml>=3.1.0',
    'pyOpenSSL>=22.1.0',
    'dotmap>=1.3.24',
    'six>=1.11.0',
]


def read_file(*parts):
    with open(os.path.join(here, *parts), 'r', encoding='utf-8') as fp:
        return fp.read()


def find_version(*paths):
    version_file = read_file(*paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='libesocial_tiastra',
    version=find_version('esocial', '__init__.py'),
    description='Biblioteca para uso com o eSocial',
    long_description=(
        'Biblioteca para uso com o eSocial.\n\n'
        'Este projeto é um fork da biblioteca "libesocial" '
        '(https://github.com/qualitaocupacional/libesocial). Agradecemos ao(s) autor(es) original(is) '
        'por seu trabalho e contribuição.\n\n'
        'Veja o README para mais detalhes sobre as modificações e o uso.'
    ),
    long_description_content_type='text/markdown',
    url='https://github.com/Tiastra/libesocial_tiastra',
    author='C.Tiago',
    author_email='tiagovza@hotmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=['contrib', 'docs']),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.10',
    ],
)

# Run tests:
# python setup.py test
