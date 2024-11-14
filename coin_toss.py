# coin_toss.py

import random

def toss_coin():
    return "Heads" if random.choice([True, False]) else "Tails"

# Sample usage
print("Coin Toss Result:", toss_coin())
