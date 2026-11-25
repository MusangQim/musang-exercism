#include "queen_attack.h"
#include <stdlib.h>
#include <stdbool.h>

attack_status_t can_attack(position_t queen_1, position_t queen_2)
{
    bool same_row;
    bool same_column;
    bool same_diagonal;

    // Validate Position
    if (queen_1.row >= 8 || queen_1.column >= 8 ||
        queen_2.row >= 8 || queen_2.column >= 8)
            return (INVALID_POSITION);

    if (queen_1.row == queen_2.row &&
        queen_1.column == queen_2.column)
        return (INVALID_POSITION);

    // Same Row
    same_row = queen_1.row == queen_2.row;

    // Same Column
    same_column = queen_1.column == queen_2.column;

    // Same Diagonal
    same_diagonal = 
        abs((int)queen_1.row - (int)queen_2.row) == 
        abs((int)queen_1.column - (int)queen_2.column);

    if (same_row || same_column || same_diagonal)
        return CAN_ATTACK;
    return CAN_NOT_ATTACK;
}
