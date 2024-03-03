# Dictionary Module

import sys
sys.path.append('/home/hcode/workspace')

from Lovekesh_hcode import Dictionary

def play_game():
    print("In Play game")


def main():
    result = play_game()

if __name__ == '__main__':
    main()
    

#built-in modules

import urllib
# urllib.urlopen("")
print(dir(urllib))


#Excercise

import re

find_members = []

for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

