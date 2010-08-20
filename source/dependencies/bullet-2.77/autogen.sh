#!/bin/sh
echo "running aclocal"
aclocal

echo "running libtool"
libtoolize --force --automake --copy

echo "running automake"
automake --add-missing --copy

echo "running autoheader"
autoheader

echo "running autoconf"
autoconf
