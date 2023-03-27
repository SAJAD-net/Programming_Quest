#!/usr/bin/env sh

if [ $1 ];then
	echo ${#1}
else
	echo "len usage --> len <STRING>"
	echo -e "example:\n\tlen abcd1234"
fi
