import gen_customer
import Plane as Pl
import random

for aLine in Pl.SkyAir.airlines:
    for flight in aLine.flights:
        start = random.getrandint(0, 24)
        finish = random.getrandint(0, 24)
        
        flight.changeDest(start, finish)
