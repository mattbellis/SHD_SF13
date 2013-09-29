import ROOT
import h5py

def root2hdf5(in_file, out_file):
    out_group = out_file.create_group('data')
    in_tree = in_file.Get('data')

    for i in xrange(in_tree.GetEntries()):
        out_dataset = out_group.create_dataset(str(i), (in_tree.GetEntry(i), in_tree.NJet, 5))
        print out_dataset
        out_dataset[i,:,0] = in_tree.Jet_E
        out_dataset[i,:,1] = in_tree.Jet_Px
        out_dataset[i,:,2] = in_tree.Jet_Py
        out_dataset[i,:,3] = in_tree.Jet_Pz
        out_dataset[i,:,4] = in_tree.Jet_btag

def main():
    import sys
    in_file = ROOT.TFile(sys.argv[1])
    out_file = h5py.File(sys.argv[2], 'w')
    root2hdf5(in_file, out_file)

if __name__ == '__main__':
    main()
