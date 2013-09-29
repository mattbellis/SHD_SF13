# Convert a ROOT file to HDF5

Physicists use [ROOT](http://root.cern.ch/) because that's what they
know. The ROOT software stores its data in a ROOT file format that
no other software can read. This is fine if you're only using the ROOT
software, but physicists are the only people who use ROOT, and even
physicists sometimes want to use  something else. So wouldn't it be nice 
to convert ROOT files into a more standard format?

I wrote an example program for how to convert a ROOT file to HDF5,
a more standard file format. The program expects a very particular
dataset; it doesn't detect the schema of the dataset. Thus, it won't
automatically convert arbitrary files. Instead, the script serves as
a template for when you should need to do such a conversion.

## How to run

First, install the dependencies. You need

* ROOT
* Python 2.7
* `/usr/lib/root` in your `PYTHONPATH`
* `wget`

On Arch Linux, you can just run.

    make dep

Once you have the dependencies, this is how you download the datasets
and run the demo.

    make

The file that is running all of this is `root2hdf5.py`.
