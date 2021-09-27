import random as rand

def generate_numbers(n):  #generating numbers
    numbers_picked = []

    while len(numbers_picked) < n:
        num = rand.randint(1, 45)

        if num not in numbers_picked:
            numbers_picked.append(num)

    return numbers_picked



def draw_winning_numbers():   #generating winning numbers
    numbers_drawn = []

    while len(numbers_drawn) < 6:
        num = rand.randint(1, 45)

        if num not in numbers_drawn:
            numbers_drawn.append(num)

        sorted_drawn_numbers = sorted(numbers_drawn)
        bonus_number = rand.randint(1, 45)
        sorted_drawn_numbers.append(bonus_number)

    return sorted_drawn_numbers




def count_matching_numbers(numbers, winning_numbers):   #counting how many match
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
        else:
            continue
    return count




def check(numbers, winning_numbers):   #checking price
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0