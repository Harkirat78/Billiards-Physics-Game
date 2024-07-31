#Harkirat Soomal

# Makefile for Assignment 2

CC = clang
CFLAGS = -std=c99 -Wall -pedantic -fpic
LDFLAGS = -lm

all: libphylib.so _phylib.so

clean:
	rm -rf *.o *.so *.pyc *.svg _phylib.so phylib_wrap.c phylib.py __pycache__ phylib.db

libphylib.so: phylib.o
	$(CC) phylib.o -shared -o libphylib.so  

phylib.o: phylib.c phylib.h
	$(CC) $(CFLAGS) -c phylib.c -o phylib.o

_phylib.so: phylib_wrap.o libphylib.so
	$(CC) phylib_wrap.o -shared -o _phylib.so -L. -L/usr/lib/python3.11 -lphylib -lpython3.11

phylib_wrap.o: phylib_wrap.c phylib.h
	$(CC) $(CFLAGS) -c phylib_wrap.c -o phylib_wrap.o -I/usr/include/python3.11/

phylib_wrap.c phylib.py: phylib.h
	swig -python -o phylib_wrap.c phylib.i

