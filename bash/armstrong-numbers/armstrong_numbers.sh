#!/usr/bin/env bash


number="$1"
no_digit=${#number}
sum=0

for ((i=0; i<no_digit; i++)); do
	digits="${number:i:1}"
	expansion=$((digits ** no_digit))
	# echo "$expansion"
	total=$((total + expansion))
done

if [[ "$number" -eq "$total" ]]; then
	echo "true"
else
	echo "false"
fi

# echo "Total calculation: $total"
# echo "No of digits: $no_digit"
