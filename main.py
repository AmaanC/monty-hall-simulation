# A simulation of the Monty Hall problem
# https://en.wikipedia.org/wiki/Monty_Hall_problem

import random

total_doors = 3
num_doors_opened = 1 # How many doors does Monty open?
trials = 100000

got_car = 0
got_goat = 0
door_list = list(range(1, total_doors + 1))

def pick_door():
    return random.randint(1, total_doors)

def place_car():
    return random.randint(1, total_doors)

def show_goat(car, chosen_door):
    doors = door_list[:]
    if car in doors:
        doors.remove(car)
    if chosen_door in doors:
        doors.remove(chosen_door)
    return random.sample(doors, num_doors_opened)

# args is the doors that have been opened by Monty or that the player chose. Get the other closed doors
def get_closed_doors(*args):
    doors = door_list[:]
    for arg in args:
        if arg in doors:
            doors.remove(arg)
    return doors

def run_test():
    global got_car
    global got_goat
    doors = door_list[:]
    car = place_car()
    chosen_door = pick_door()
    open_doors = show_goat(car, chosen_door)
    doors_to_switch_to = get_closed_doors(chosen_door, *open_doors)
    chosen_door = random.choice(doors_to_switch_to)

    if chosen_door == car:
        got_car += 1
    else:
        got_goat += 1

def main():
    for _ in range(trials):
        run_test()
    print(
        ('Monty shows you {} goat(s) out of {} doors.\n'
        'Odds of getting the car if you always switch are {}. Found running {} trials')
        .format(num_doors_opened, total_doors, got_car / (got_car + got_goat), trials)
    )

if __name__ == '__main__':
    main()