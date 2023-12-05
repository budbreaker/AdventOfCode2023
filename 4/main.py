import time


def process_card(id, cards):
    summ = 0
    numbers = cards[id].split(":")[1].split("|")
    winning_numbers = numbers[0].split()
    drawn_numbers = numbers[1].split()
    wins = sum(1 for num in winning_numbers if num in drawn_numbers)
    for i in range(wins):
        summ += process_card(id + i + 1, cards)
    return summ + 1


with (open("input.txt") as f):
    start_time = time.time()
    cards = f.readlines()
    summ = 0
    card_count = 0
    card_counts = [1]*len(cards)
    for i in range(len(cards)):
        print(cards[i].strip())
        numbers = cards[i].split(":")[1].split("|")
        winning_numbers = numbers[0].split()
        drawn_numbers = numbers[1].split()
        wins = sum(1 for num in winning_numbers if num in drawn_numbers)
        for j in range(wins):
            card_counts[i + j + 1] += card_counts[i]
        if wins > 0:
            summ += 2 ** (wins - 1)
        card_count += process_card(i, cards)
    print(summ)
    print(card_count)
    print(sum(card_counts))
    print("--- %s seconds ---" % (time.time() - start_time))
