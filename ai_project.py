from random import random
import random
from re import X

from typing import List
##
list = ["A","B","C","D","E"]
random.shuffle(list)
parentList = []
parent1 = random.sample(list,5)
parent1.append(parent1[0])
parentList.append(parent1)
parent2 = random.sample(list,5)
parent2.append(parent2[0])
parentList.append(parent2)
parent3 = random.sample(list,5)
parent3.append(parent3[0])
parentList.append(parent3)
parent4 = random.sample(list,5)
parent4.append(parent4[0])
parentList.append(parent4)
parent5 = random.sample(list,5)
parent5.append(parent5[0])
parentList.append(parent5)
parent6 = random.sample(list,5)
parent6.append(parent6[0])
parentList.append(parent6)
parent7 = random.sample(list,5)
parent7.append(parent7[0])
parentList.append(parent7)
parent8 = random.sample(list,5)
parent8.append(parent8[0])
parentList.append(parent8)

print(*parentList, sep="\n")
print("Αυτός είναι ο αρχικός πληθυσμός αποτελούμενος απο 8 χρωμοσώματα τα οποία θα διασταυρωθούν ! ")

## θα κάνουμε 10 γενιές



def CostCount(offspring):
   for i in range(len(offspring)):
       print(offspring[i])


def CrossOver(parent1,parent2):
    temp1 = parent1[0:3]
    temp2 = parent2[0:3]
    print(temp1)
    print(temp2)






graph = {"A":{"B":4,"C":4,"D":7,"E":3},
           "B":{"C":2,"D":3,"E":5,"A":4},
           "C":{"B":2,"D":2,"E":3,"A":4},
           "D":{"B":3,"C":2,"A":7,"E":6},
           "E":{"A":3,"B":5,"C":3,"D":6}
        }
CostCount(parent1)
'''

offsping1 = []
offsping2 = []
def CrossOver(parent1,parent2):
    part1 = parent1[3:]
    part2 = parent2[3:]
    for x in parent1[:3]:
        offsping1.append(x)
    for x in part2:
        offsping1.append(x)
    for x in parent2[:3]:
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
print(offsping1,offsping2)
#Mutation(offsping1)
'''
