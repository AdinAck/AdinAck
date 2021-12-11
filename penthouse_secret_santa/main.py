from random import shuffle
import json

from send_email import Mailer


def santify(people):
    # Generate a random permutation of the list of names.
    random_permutation = list(people.keys())
    shuffle(random_permutation)

    # Create a list of pairs of names.
    for i in range(len(random_permutation)):
        yield random_permutation[i], random_permutation[(i + 1) % len(random_permutation)]


with open('participants.json', 'r') as f:
    people = json.load(f)

m = Mailer()

for p1, p2 in santify(people):
    intro = f"Hello, {p1}!\n\nIt's time for the one and only Penthouse Secret Santa!!!\n\nYour giftee is {p2}.\n\n{p2}'s gift preferences are as follows: \n\n"
    preferences = '\n'.join(
        '- '+line for line in people[p2]['Preferences']) + '\n\n'
    outro = "Choose your gift wisely!\n\n - Penthouse Bot"
    m.send_email(people[p1]['Email'],
                 'Penthouse Secret Santa', intro+preferences+outro)
