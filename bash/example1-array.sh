#!/bin/bash

array=( "one" "two" "three" );
files=( "/etc/passwd" "/etc/group" "/etc/hosts" );
limits=( 10 20 30 40)

printf "%s\n" "${array[@]}";
printf "%s\n" "${files[@]}";
printf "%s\n" "${limits[@]}";
