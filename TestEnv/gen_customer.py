import Plane
import numpy as np
import random
# get a list of names to generate customers

last = open("lastname.txt", "r")
lastNames = last.readlines()
last.close()

first = open("firstname.txt", "r")
firstNames = first.readlines()
first.close()
# setup an array for now may change later for optimization
lastNP = np.array(lastNames)
firstNP = np.array(firstNames)

list = []

for i in range(1000):
    randL = random.randRange(0, len(lastNP))
    randF = random.randRange(0, len(firstNP))

    list.append(Plane.Customer.create_customer(firstNP[randF], lastNP[randL]))
