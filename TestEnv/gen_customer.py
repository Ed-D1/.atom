import Plane
import numpy as np
import random
# get a list of names to generate customers

last = open("TestEnv/lastname.txt", "r")
lastNames = last.readlines()
last.close()

first = open("TestEnv/firstname.txt", "r")
firstNames = first.readlines()
first.close()
# setup an array for now may change later for optimization
lastNP = np.array(lastNames)
firstNP = np.array(firstNames)

Customer_list = []

for i in range(1000):
    randL = random.randrange(0, len(lastNP))
    randF = random.randrange(0, len(firstNP))

    Customer_list.append(Plane.Customer(firstNP[randF], lastNP[randL]))
