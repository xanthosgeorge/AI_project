from random import random
import random
from re import X

from typing import List
list = ["A","B","C","D","E"]
random.shuffle(list)
parent1 = random.sample(list,5)
parent2 = random.sample(list,5)
#print(parent1,parent2)

graph = {"A":{"B":4,"C":4,"D":7,"E":3},
           "B":{"C":2,"D":3,"E":5,"A":4},
           "C":{"B":2,"D":2,"E":3,"A":4},
           "D":{"B":3,"C":2,"A":7,"E":6},
           "E":{"A":3,"B":5,"C":3,"D":6}
        }

offsping1 = []
offsping2 = []
def CrossOver(parent1,parent2):
    part1 = parent1[4:]
    part2 = parent2[4:]
    #print(part1,part2)
    for x in parent1[:4]:
        offsping1.append(x)
    for x in part2:
        offsping1.append(x)
    for x in parent2[:4]:
        offsping2.append(x)
    for x in part1:
        offsping2.append(x)  # the last two elements of each parent are being changed


def Mutation(offsping1):
    listOfReplacements = list
    for x in offsping1[:4]:
        listOfReplacements.remove(x)
    print(offsping1)
    print(listOfReplacements)
    offsping1.pop(-1)
    offsping1.append(listOfReplacements[0])
    print(offsping1)
            
    

        
    


CrossOver(parent1,parent2)
Mutation(offsping1)
""" print (parent1,parent2)
print(offsping1,offsping2) """