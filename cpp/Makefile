# Makefile
#
# Rules for making Project Euler C++ binaries.
#
# Author: Curtis Belmonte
# Created: Aug 18, 2014

# MACROS ######################################################################

CC = g++
CFLAGS = 

# NON-FILE TARGETS ############################################################

clobber: clean
	rm -f *~ \#*\# core

clean:
	rm -f problem??? *.o

# FILE TARGETS ################################################################

problem%: problem%.o common.o
	$(CC) $(CCFLAGS) $< common.o -o $@

problem%.o: problem%.cpp common.h
	$(CC) $(CCFLAGS) -c $< 

common.o: common.cpp common.h
	$(CC) $(CCFLAGS) -c $<
