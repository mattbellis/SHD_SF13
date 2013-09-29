import numpy as np
import ROOT
import h5py

def root2hdf5(in_file, out_file):
    out_group = out_file.create_group('data')
    in_tree = in_file.Get('data')

    for i in xrange(in_tree.GetEntries()):
        out_dataset = out_group.create_dataset(str(i), (in_tree.GetEntry(i), in_tree.NJet, 5))
        for j in xrange(in_tree.GetEntry(i)):
            out_dataset[i,j,0] = in_tree.Jet_E[j]
            out_dataset[i,j,1] = in_tree.Jet_Px[j]
            out_dataset[i,j,2] = in_tree.Jet_Py[j]
            out_dataset[i,j,3] = in_tree.Jet_Pz[j]
            out_dataset[i,j,4] = in_tree.Jet_btag[j]

def main():
    import sys
    in_file = ROOT.TFile(sys.argv[1])
    out_file = h5py.File(sys.argv[2], 'w')
    root2hdf5(in_file, out_file)

if __name__ == '__main__':
    main()
