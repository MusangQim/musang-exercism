#include "difference_of_squares.h"

unsigned int square_of_sum(unsigned int number)
{
	int s;
	int calculation;

	s = number * (number + 1) / 2;
	calculation = s * s;
	return calculation;

}

unsigned int sum_of_squares(unsigned int number)
{
	int calculation;

	calculation = number * (number + 1) * (2 * number + 1) / 6;
	return calculation;

}
unsigned int difference_of_squares(unsigned int number)
{
	return square_of_sum(number) - sum_of_squares(number);

}
