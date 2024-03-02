"""
This program calculates when a person will
turn 100 yrs old.
Information required:
- name of user
- age of user
"""

"Using variable 'nameU' & 'ageU' to collect the information."
nameU = input("Give me your name: ")
ageU = int(input("How old are you: "))
curYr = int(input("Which year is this: "))

"This formula calculates when user will turn 100 yrs old."
turning100 = 100 - ageU
turning100_yr = curYr - ageU + 100

"Returning the output."
print(f"{nameU}, you will turn 100 in {turning100} yrs in the year {turning100_yr} ")
