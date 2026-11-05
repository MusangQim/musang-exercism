#!/usr/bin/env bash

two-fer()
{
	name="$1"

	if [[ -z "$name" ]]; then
		name="you"
	fi

	echo "One for $name, one for me."
}
two-fer "$1"
