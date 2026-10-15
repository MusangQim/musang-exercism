#include "grains.h"

uint64_t square(uint8_t index)
{
	uint64_t grains;

	if (index < 1 || index > 64)
		return 0;
	grains = 1ULL << (index - 1);
	return grains;
}

uint64_t total(void)
{
	uint64_t total_grains;

	total_grains = UINT64_MAX;
	return total_grains;
}

