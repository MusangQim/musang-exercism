#include "collatz_conjecture.h"

// Even Number = Divide 2 (x / 2)
// Odd Number = Multiply 3 and Add 1 (3x + 1)

int steps(int start)
{
    int number;
    int count;

    if (start < 1)
        return ERROR_VALUE;
    number = start;
    count = 0;
    while (number != 1)
    {
        if (number % 2 == 0)
            number = number / 2;
        else
            number = 3 * number + 1;
        count++;
    }
    return (count);
}

