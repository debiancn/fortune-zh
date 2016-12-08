#!/bin/bash
# Count strings in data files for fortune-zh
# Zhou Mo <cdluminate@gmail.com>

#set -e

DICT="tang300 song100 chinese"

printf "\x1B[33m"

for ITEM in ${DICT}; do
	printf "%2s${ITEM}:\t" 
	grep -c '^%' ${ITEM}
done

total=$((
  $(grep -c '^%' tang300) +
  $(grep -c '^%' song100) +
  $(grep -c '^%' chinese)
))
echo ":: " \
  $(( 100 * $(grep -c '^%' tang300) / $total ))% \
  $(( 100 * $(grep -c '^%' song100) / $total ))% \
  $(( 100 * $(grep -c '^%' chinese) / $total ))%

printf "\x1B[m"
