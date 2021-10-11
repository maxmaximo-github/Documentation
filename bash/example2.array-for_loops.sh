#!/bin/bash

list=( "Hello World" "how are you?" "I'm a fine" );

for i in "${list[@]}";
do
    printf "%s\n" "$i";

done;
