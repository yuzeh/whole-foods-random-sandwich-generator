#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import math
import random

BREAD = [
    'Sliced Whole Grain',
    'Sliced Sourdough',
    'Sliced Rye',
    'Ciabatta Roll',
    'Dutch Crunch Roll',
    'French Roll',
    'Sourdough Roll',
    'Whole Wheat Roll',
    'Foccacia Roll',
    'French Baguette',
    'Gluten Free Sliced',
    'Wheat Wrap',
    'Whole Grain Lavash',
    'PantoFolina Roll',
]

VEGGIES = [
    'Lettuce',
    'Spinach',
    'Spring Mix',
    'Tomato',
    'Red Onion',
    'Pickle',
    'Pepperoncini',
    'Arugula',
    'Roasted Red Pepper',
    'Balsamic Onions',
    'Jalapeño',
    'Cucumber',
    'Artichoke Hearts',
    'Kale',
    'Pickled Carrots & Daikon',
]

MAIN = [
    'Roast Turkey',
    'Smoked Turkey',
    'Roast Beef',
    'Lemongrass Pork Loin',
    'Ham',
    'Salami',
    'Tuna Salad',
    'Egg Salad',
    'Lemon Herb Grilled Chicken',
    'Chili Grilled Chicken',
    'Grilled Veggies',
    'Grilled or Sesame Tofu',
    'Falafel',
]

CHEESE = [
    'Cheddar',
    'Swiss',
    'Provolone',
    'Jack',
    'Pepper Jack',
    'Havarti',
]

SPREADS = [
    'Mayonnaise',
    'Yellow Mustard',
    'Dijon Mustard',
    'Honey Mustard',
    'Olive Tapenade',
    'Cranberry Relish',
    'Pesto',
    'Oil',
    'Red Wine Vinegar',
    'Balsamic Vinegar',
    'Balsamic Vinaigrette',
    'Sundried Tomato Aioli',
    'Garlic Aioli',
    'Just Mayo (Vegan)',
    'Hummus',
    'Sriracha',
]

parser = argparse.ArgumentParser(description = 'Generates a random Whole Foods sandwich.')
parser.add_argument('--min_veggies', type = int, default = 1)
parser.add_argument('--max_veggies', type = int, default = len(VEGGIES))
parser.add_argument('--min_spreads', type = int, default = 1)
parser.add_argument('--max_spreads', type = int, default = 2)

def choose(n, k):
  return math.factorial(n) / math.factorial(k) / math.factorial(n - k)

def sample_index_weighted(weights):
  weight_sum = sum(weights)
  normalized = [float(w) / weight_sum for w in weights]
  random_value = random.random()
  for i, w in enumerate(normalized):
    if random_value < w:
      return i
    else:
      random_value -= w
  return i # In case of floating point error

def sample(items, a, b):
  '''Picks k items at random, where a <= k <= b, and such that all possible outputs of this
  function have equal probability (specifically, a combination with i items and a combination with
  j items will have the same probability, even if i != j.'''

  possible_k = range(a, b + 1)
  weights = [choose(len(items), i) for i in possible_k]
  k = possible_k[sample_index_weighted(weights)]

  return random.sample(items, k)

def main():
  args = parser.parse_args()

  bread = random.choice(BREAD)
  veggies = sample(VEGGIES, args.min_veggies, args.max_veggies)
  main = random.choice(MAIN)
  cheese = random.choice(CHEESE)
  spreads = sample(SPREADS, args.min_spreads, args.max_spreads)
  grill = random.random() > 0.5

  print 'Bread:', bread
  print 'Veggies:', veggies
  print 'Main:', main
  print 'Cheese:', cheese
  print 'Spreads:', spreads
  print 'Grill:', grill

if __name__ == '__main__':
  main()
