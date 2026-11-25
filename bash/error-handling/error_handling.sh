#!/usr/bin/env bash

# $# -ne 1 = No of argument not equal to 1?
if [[ $# -ne 1 ]]; then
    echo "Usage: error_handling.sh <person>"
    exit 1
fi
echo "Hello, $1"
