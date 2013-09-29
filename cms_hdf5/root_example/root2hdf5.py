import numpy as np
import ROOT
import h5py

def root2hdf5(infile, outfile):
    outgroup = outfile.create_group('data')
    intree = infile.Get('data')

    outdataset = outgroup.create_dataset('NJet', (intree.GetEntries(), intree.NJet, 5))
    for i in xrange(intree.GetEntries()):
        j = intree.GetEntry(i)
        for j in xrange(intree.NJet):
            outdataset[i,j,0] = intree.Jet_E[j]
            outdataset[i,j,1] = intree.Jet_Px[j]
            outdataset[i,j,2] = tree.Jet_Py[j]
            outdataset[i,j,3] = tree.Jet_Pz[j]
            outdataset[i,j,4] = tree.Jet_btag[j]

def main():
    import sys
    infile = ROOT.TFile(sys.argv[1])
    outfile = h5py.File(sys.argv[2], 'w')
    root2hdf5(infile, outfile)

if __name__ == '__main__':
    main()
