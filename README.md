Pyalmanac
=========

Pyalmanac is a Python script that creates the daily pages of the Nautical Almanac. These are tables that are needed for celestial navigation with a Sextant.

This fork of the original code (which can be found at: https://github.com/rodegerdts/Pyalmanac) aims to include a brief guide to celestial navigation and tables of other numbers required to take a sextant measurement and produce a line of position.  

WARNING
-------

These tables are generated without warranty or guarantee and should be used with caution.  The original author states on his web page (https://sv-inua.net/the-nautical-almanac) that he has tested the code against a 2009 Nautical Almanac (which is published by the UK and US) and could not find any errors over 0.3'.


Requirements
------------

Most of the heavy computing is done by the free Pyephem library.
Typesetting is done by TeX/LaTeX So before you can use this program you need to install:

Python v2.x (2.6 or later ) python 3 will not work out of the box

PyEphem

TeX/LaTeX


INSTALLATION Linux:

Install your platforms Python- and LaTeX distribution. Remember to chose python 2.x and install all develpment header files.
Run at the command line:

pip install pyephem

Put the Pyalmanac files in any directory and start with:

python pyalmanac
or
./pyalmanac



INSTALLATION MAC:

Every Mac comes with python preinstalled. You need to install the PyEphem library to use Pyalmanac. Type the following commands at the commandline (terminal app):

sudo easy_install pip

pip install pyephem

If this command fails your mac asks you if you would like to install the header files. Do so, you do not need to install the full IDE.
Try again.

Install TeX/LaTeX from http://www.tug.org/mactex/

Now you are almost ready
Put the Pyalmanac files in any directory and start with
python pyalmanac
or
./pyalmanac
