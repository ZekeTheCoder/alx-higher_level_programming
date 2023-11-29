#!/usr/bin/python3
uppercase = False
for i in range(122, 96, -1):
    character = i
    if uppercase:
        character -= 32
        uppercase = False
    else:
        uppercase = True
    print("{:c}".format(character), end='')
