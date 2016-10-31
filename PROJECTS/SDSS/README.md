# SDSS Photometric Lens Search

SDSS DR10 is a useful testbed for us: it provides easily-queried objects for testing catalog selection methods. We might even find some new lenses, digging down to below the SQLS spectroscopic pre-selection limit (i < 19). The classification algorithms developed in this repo will ideally be easily portable to work on simulated PS1 catalogs produced using [independent code](https://github.com/drphilmarshall/OM10).

The goal of making this repo functional is to complete the object-oriented framework that already partially exists in [PS1QLS.py](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/PS1QLS.py). This code creates a Dataset object to handle inputs, and has Classifier objects act on Datasets to produce lens/dud classification probabilities. 

* [OOP_Classifier.ipynb](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/OOP_Classifier.ipynb) is a notebook with some tests I checked as I was developing PS1QLS.py. 
* [Using OOP Classifier.ipynb](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/Using%20OOP%20Classifier.ipynb) provides examples of using the PS1QLS.py interface.

Exploring the Data:

* [SDSS_object_pre-selection.ipynb](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/SDSS_object_pre-selection.ipynb) provides a recipe for getting new examples of SDSS galaxies from the Sloan SkyServer.

* [exploring_eric_catalog.ipynb](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/exploring_eric_catalog.ipynb) This notebook will help eventually allow this code to operate on simulated PS1 data, as it demonstrates the content of and interface with such simulated catalogs.

* [trying_out_OM10.ipynb](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/trying_out_OM10.ipynb) is a short demo of the interface to the OM10 package that will eventually produce simulated catalogs for us. 

The other notebooks found in this repo explore various sub-parts of the classification task, as described below:

* The text at the beginning of [analyzing_adri_sims.ipynb](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/analyzing_adri_sims.ipynb) gives an overview on how extreme deconvolution (XD) can be used as a photometric lensed quasar classifier (definitely give it a read!). Along with its companion notebook [XD_Classifier.ipynb](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/XD_Classifier.ipynb), it shows how to implement an XD classifier on artifically noisified data. This might seem like a silly thing to do, but the only way we'll know that XD can infer the true distribution underlying a noisy one is if we know what the noise is in the first place!

* [ML_methods.ipynb](https://github.com/drphilmarshall/PS1QLS/blob/master/PROJECTS/SDSS/ML_Methods.ipynb): This notebook is an introduction to the scikit-learn interface we want to use for our classifiers as well. It demonstrates random forests (RFs) and support-vector machines (SVMs), two popular machine learning methods we will use as a performance baseline.


