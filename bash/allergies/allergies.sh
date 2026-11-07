#!/usr/bin/env bash

allergic_to()
{
	local score="$1" item="$2" value
	case "$item" in
		eggs)
			value=1;;
		peanuts)
			value=2;;
		shellfish)
			value=4;;
		strawberries)
			value=8;;
		tomatoes)
			value=16;;
		chocolate)
			value=32;;
		pollen)
			value=64;;
		cats)	
			value=128;;
		*)	
			value=0;;
	esac

	if ((score & value)); then
		echo "true"
	else
		echo "false"
	fi	
	
}

list()
{
	local score="$1"
	local item
	local result=""

	for item in eggs peanuts shellfish strawberries tomatoes chocolate pollen cats; do
		if [[ $(allergic_to "$score" "$item") == "true" ]]; then
			result+="$item "
		fi
	done
	echo "${result% }"
}

allergy_score()
{
	local score=0 item value
	for item in "$@"; do
		case "$item" in
			eggs)
				value=1;;
			peanuts)
				value=2;;
                	shellfish)
                        	value=4;;
                	strawberries)
                        	value=8;;
                	tomatoes)
                        	value=16;;
                	chocolate)
                        	value=32;;
                	pollen)
                        	value=64;;
               		cats)
                        	value=128;;
                	*)
                        	value=0;;
		esac
		score=$((score + value))
	done
	echo "$score"
}

case "$2" in
    allergic_to)
        allergic_to "$1" "$3"
        ;;
    list)
        list "$1"
        ;;
    allergy_score)
        shift 2
        allergy_score "$@"
        ;;
esac
