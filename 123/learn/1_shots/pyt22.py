# When provided with a number between 0-9, return it in words. Note that the input is guaranteed to be within the range of 0-9.
# Input: 1
# Output: "One".
# If your language supports it, try using a switch statement.


def switch_it_up(number):
    answer = "incorrect value"

    match number:
        case 0:
            answer = "Zero"
        case 1:
            answer = "One"
        case 2:
            answer = "Two"
        case 3:
            answer = "Three"
        case 4:
            answer = "Four"
        case 5:
            answer = "Five"
        case 6:
            answer = "Six"
        case 7:
            answer = "Seven"
        case 8:
            answer = "Eight"
        case 9:
            answer = "Nine"
    return answer


print(switch_it_up(5))