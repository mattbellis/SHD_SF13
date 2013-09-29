# Convert a ROOT file to HDF5

Physicists use [ROOT](http://root.cern.ch/) because that's what they
know. But nobody else uses ROOT, and physicists sometimes want to use 
something else, so it would be nice to convert ROOT files into a more
standard format, like HDF5.

I wrote an example script of how to convert a ROOT file to HDF5.
The script expects this particular dataset; it doesn't detect the
schema of the dataset. Thus, it won't automatically convert arbitrary
files. Instead, the script serves as a template for when you should
need to do such a conversion.

## How to run

Install dependencies. You need

* ROOT
* Python 2.7
* `/usr/lib/root` in your `PYTHONPATH`
* `wget`

On Arch Linux, you can just run.

    make dep

Once you have the dependencies, this is how you download the datasets
and run the demo.

    make
