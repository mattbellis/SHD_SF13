import numpy as np
import matplotlib.pylab as plt
import sys

import family_utilities as famu 

f = open(sys.argv[1])

print "Reading in the data...."
families = famu.get_families(f)

print len(families)

print "Looping over the families..."
for family in families:

    parents = family[0]
    children = family[1]
    pets = family[2]
    family_info = family[3]

    household_income = family_info[0]
    latitude = family_info[1]
    longitude = family_info[2]
    
    print "# of parents: %d" % (len(parents))
    if len(parents)>0:
        print "parents", parents
    print "# of children: %d" % (len(children))
    if len(children)>0:
        print children


