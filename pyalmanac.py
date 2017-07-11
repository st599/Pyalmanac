#! /usr/bin/python
# -*- coding: UTF-8 -*-

#	Copyright (C) Copyright for portions of project Foo are held by
#      Enno Rodegerdts, 2014 as part of project PyAlmanac. All other copyright
#      for project PyAlmanac-st599 are held by Simon Thompson, 2017.

#	Updates Simon Thompson 2017

#  This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 2 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License along
#     with this program; if not, write to the Free Software Foundation, Inc.,
#     51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


"""
This  module contains the main class for PyAlmanac.  It uses PyEphem to generate
Sun Almanac or Nautical Almanac for a given year.
"""

__author__ = "Enno Rodegerdts and Simon Thompson"
__copyright__ = "Copyright for portions of project Foo are held by Enno Rodegerdts, 2014 as part of project PyAlmanac. All other copyright for project PyAlmanac-st599 are held by Simon Thompson, 2017."
__license__ = "GPL v2"
__version__ = "2.0.1"
__maintainer__ = "Simon Thompson"
__status__ = "Beta"

import tables
import suntables
import os


##Main###
if __name__ == '__main__':


	## GPL Licence Condition
	print "------------------------------------------------------------------------------"
	print "PyAlmanac version %s - Generate Nautical Almanac for Astro-Navigation" %__version__
	print "Released under %s" %__license__
	print "Maintained by %s" %__maintainer__
	print "-------------------------------------------------------------------------------"

	print "Copyright for portions of project PyAlmanac-st599 are held by Enno Rodegerdts, 2014 as part of project PyAlmanac. All other copyright for project PyAlmanac-st599 are held by Simon Thompson, 2017.\n"
	print "This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.\n"
	print "This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.\n"
	print "You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.\n"

	print "------------------------------------------------------------------------------"
	print ""

	year =  raw_input("Please enter the year you want to create the nautical almanac for:\n ")
	s =  raw_input("""Do you want to create the full tables or just tables for the sun?:\n
	1	Full nautical almanac
	2	Just tables for the sun
	""")
	if s == "2":
		print "Creating the sun tables only. \n The year %s" %year
		print "Please wait this can take a while."
		filename = "sunalmanac%s.tex" %year
		outfile = open(filename, 'w')
		outfile.write(suntables.almanac(year))
		outfile.close()
		command = 'pdflatex %s' %filename
		os.system(command)
		print "finished"
		os.remove("sunalmanac%s.log" %year)
		os.remove("sunalmanac%s.aux" %year)
		os.remove(filename)
	elif s == "1":
		print "Creating the nautical almanac for the year %s" %year
		print "Please wait this can take a while."
		filename = "almanac%s.tex" %year
		outfile = open(filename, 'w')
		outfile.write(tables.almanac(year))
		outfile.close()
		command = 'pdflatex %s' %filename
		os.system(command)
		print "finished"
		os.remove(filename)
		os.remove("almanac%s.log" %year)
		os.remove("almanac%s.aux" %year)
	else:
		print "Error! Choose either 1 or 2"
