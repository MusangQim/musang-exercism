#!/usr/bin/env bash

armstrong()
{
	number="$1"
	no_digit=${#number}
	total=0

	for ((i=0; i<no_digit; i++)); do
		digits="${number:i:1}"
		expansion=$((digits ** no_digit))
		total=$((total + expansion))
	done

	# echo "Digits: $no_digit"
	# echo "Total calculation: $total"

	if [[ "$number" -eq "$total" ]]; then
		echo "true"
		return 0
	else
		echo "false"
		return 0
	fi
}
armstrong "$1"
