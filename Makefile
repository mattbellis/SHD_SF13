run: deps gunzip
	python2 root2hdf5.py HEPTutorial/files/mc_qcd.root mc_qcd.hdf5

deps:
	which root || yaourt -S root

download:
	test -e HEPTutorial.tar_.gz || wget http://ippog.web.cern.ch/sites/ippog.web.cern.ch/files/HEPTutorial.tar_.gz

gunzip: download
	test -e HEPTutorial || tar xzf HEPTutorial.tar_.gz


