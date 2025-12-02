#! /usr/bin/env python3

def unlock_safe(turns: list[str]) -> None:
    dial: int = 50
    landed_on_zero: int = 0
    click_on_zero: int = 0

    for turn in turns:
        distance: int = int(turn[1:])
        if turn[0] == 'L':
            distance *= -1
        new_dial: int = dial + distance 

        if new_dial % 100 == 0:
            landed_on_zero += 1
        
        if new_dial == 0:
            # Counts as seeing zero unless we started on zero
            click_on_zero += 0 if dial == 0 else 1
        elif new_dial > 0:
            click_on_zero += new_dial // 100
        else: # i.e. new_dial < 0
            # -100 // 100 == -1, but represents seeing zero twice
            # By using new_dial-1 below we account for that unwanted behavior at multiples of -100
            click_on_zero += abs((new_dial - 1) // 100)
            # If we started with dial == 0 then don't count that initial sighting of zero
            if dial == 0:
                click_on_zero -= 1 
            
        dial = new_dial % 100

    print(f'landed_on_zero: {landed_on_zero}')
    print(f'click_on_zero: {click_on_zero}')

for input_file in ('day01_test.txt', 'day01_input.txt'):
    with open(input_file, 'r') as file:
        turns: list[str] = [l for l in file.readlines() if l.strip()]
        print(f'Results for {input_file}')
        unlock_safe(turns)
        print()
