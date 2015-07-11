Just threw some code together to simulate the Monty Hall problem. There are 3 variables that are configurable in the code:

 - `total_doors`: The total number of doors in the game (3, in the most common variant)
 - `num_doors_opened`: The number of doors that Monty Hall will open and show to you (1 in the most common variant)
 - `trials`: The number of times it plays the game. The higher this number, the more accurate your result will be, but the longer it'll take too (100,000 by default)