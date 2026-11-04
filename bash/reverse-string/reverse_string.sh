#!/usr/bin/env bash

reverse_string()
{
	string="$1"
	reversed=""
	for (( i=0; i<${#string}; i++ )); do
		character="${string:i:1}"
		reversed="$character$reversed"
	done

	echo "$reversed"
}
reverse_string "$1"
