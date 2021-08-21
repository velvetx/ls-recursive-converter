<h2>ls-recursive-converter</h2>
A very simple and lightweight program that converts the output of "ls -R > filename.txt" to a wordlist for dirbuster. 

--------

<h3>Before use:</h3>

* Use `ls -R > filename.txt` or `ls --recursive > filename.txt`
on folder with subdirectories.

--------

<h3>Installation:</h3>

* No requirements needed.

If you want to use without setup.py, just run:
* `python3 lsRecursiveConverter.py`

If you want to use with the console command:
* `python3 setup.py install`

And then run:
* `ls-recursive-converter` in terminal.

--------

<h3>Usage:</h3>

`ls-recursive-converter -p [File path] -o [Specify the path to save the result ] -f [Parse files] -d [Parse directories]`

Help menu:
* `ls-recursive-converter -h`
* `ls-recursive-converter --help`

or 
* `python3 lsRecursiveConverter.py -h`
* `python3 lsRecursiveConverter.py --help`

_<h4>Arguments:</h4>_

Required:
* `-p --path [Define the path to your filename.txt]`
* `-o --outfile [Define outfile for result]`

`ls-recursive-converter -f [File path] -o [Path to save the result]` - 
this command creates directory ls-recursive-converter/ at the given path and saves 2 files (files.txt, directories.txt)

<h4>If you don't want to keep both files:</h4>

use non-required arguments:

* `-f --files` - for save only files, without directories
*  `-d --directories` - for save only directories, without files
