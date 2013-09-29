import numpy as np
import ROOT
import h5py

def root2hdf5(infile, outfile):
    tree = infile.Get("data")
    tree.Print()

if __name__ == '__main__':
    import sys
    infile = ROOT.TFile(sys.argv[1])
    outfile = h5py.File(sys.argv[2], 'w')
    root2hdf5(infile, outfile)
