import os
import tempfile
import shutil
import setuptools
from distutils.core import setup


current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, 'README.md'), encoding='utf-8') as reader:
    read_me_description = reader.read()

env_dir = tempfile.mkdtemp(prefix='lsRecursiveConverter-install-')
shutil.copytree(os.path.abspath(os.getcwd()), os.path.join(env_dir, 'lsRecursiveConverter'))

os.chdir(env_dir)

setup(
    name='ls-recursive-converter',
    version='0.0.1',
    author='velvetx',
    platforms='GNU/Linux',
    url='https://github.com/velvetxq/ls-recursive-converter',
    license='GPL',
    description='A very simple and lightweight program that converts the output of "ls -R > filename.txt" to a '
                'wordlist for dirbuster.',
    long_description=read_me_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=['Programming Language :: Python :: 3.9'],
    package_data={
        'lsRecursiveConverter': ['*', 'src/*']
    },
    entry_points={
        'console_scripts': ['ls-recursive-converter=lsRecursiveConverter.lsRecursiveConverter:Program']
    }
)
