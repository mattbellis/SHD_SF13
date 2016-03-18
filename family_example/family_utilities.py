import numpy as np


################################################################################
################################################################################
def get_families(infile,verbose=False):

    families = []

    not_at_end = True
    family_count = 0

    while ( not_at_end ):

        ############################################################################
        # Read in one family
        ############################################################################

        if family_count%1000==0 and verbose:
            print "family count: ",family_count

        # Read in the parent info for this family.
        parents = []
        line = infile.readline()

        # Check to see if we are at the end of the file.
        if line == "":
            not_at_end = False
            break

        nparents = int(line.split()[0])
        for i in xrange(nparents):
            line = infile.readline()
            vals = line.split()
            sex = int(vals[0]) # 0: female, 1: male
            gender_identity = int(vals[1]) # 0: female, 1: male
            age = float(vals[2]) # years
            weight = float(vals[3]) # kilograms
            height = float(vals[4]) # meters
            parents.append([sex,gender_identity,age,weight,height])

        # Read in the children info for this family.
        children = []
        line = infile.readline()
        nchildren = int(line.split()[0])
        for i in xrange(nchildren):
            line = infile.readline()
            vals = line.split()
            sex = int(vals[0]) # 0: female, 1: male
            gender_identity = int(vals[1]) # 0: female, 1: male
            age = float(vals[2]) # years
            weight = float(vals[3]) # kilograms
            height = float(vals[4]) # meters
            children.append([sex,gender_identity,age,weight,height])
            

        # Read in the pet info for this family.
        pets = []
        line = infile.readline()
        npets = int(line.split()[0])
        for i in xrange(npets):
            line = infile.readline()
            vals = line.split()
            animal = int(vals[0]) # 0: dog, 1: cat, 2: fish, 3: bird, 4: monkey
            age = float(vals[1]) # years
            pets.append([animal,age])


        # Read in extra information about the family in general.
        line = infile.readline()
        vals = line.split()
        household_income = float(vals[0])
        latitude = float(vals[1])
        longitude = float(vals[2])

        family_count += 1

        families.append([parents,children,pets,[household_income,latitude,longitude]])

    return families

