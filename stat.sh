#!/bin/sh
set -e

echo -n "chinese\t"
rg '^%' chinese | wc -l
echo -n "tang300\t"
rg '^%' tang300 | wc -l
echo -n "song100\t"
rg '^%' song100 | wc -l
