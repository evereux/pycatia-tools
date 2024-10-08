pycatia-tools
=============


Introduction
============
A web based python application built with 
[Flask](https://flask.palletsprojects.com/en/latest/), [HTMX](https://htmx.org/) 
and [hyperscript](https://hyperscript.org) to interface with CATIA V5 using the 
python library [pycatia](https://pycatia.readthedocs.io/en/latest/).

The application contains a collection of tools to speed up common tasks. Such as:

* Create new Part, Product or Drawing with additional details such as 
   * Part Number, Revision, Nomenclature and Definition
   * User defined properties as defined in settings.yaml.
   * Geometric Set and Parameter values are created as defined in settings.yaml. 
     To skip the creation replace the values with `None`.
* Import to CATPart or export from CATPart points using CSV files.
* Create a bounding box around a part.
* Lock / Unlock all views of a CATDrawing.
* Turn off / on all view frames in a CATDrawing.
* Save CATDrawing to a single sheet PDF.
* Save CATDrawing to DXF.

pycatia-tools has been built such that adding additional functionality to suit
your purposes is a straight forward process. There is currently no guide 
supporting this. However, reading the source code should give enough hints on 
how to add functionality.


Requirements
============

* Windows 7 or higher.
* python >= 3.11 (earlier versions upto 3.9 may work but not yet tested)
* CATIA V5 must already be running.


Installation
============

Pre Built Binary
----------------

* Download the latest zip file from https://github.com/evereux/pycatia-tools/releases.

* Unzip the package and run pycatia-tools.exe by double clicking on it.

* In your web browser access the page http://127.0.0.1:5578/ in your browser.

git
---

To clone this repository using [git cmd](https://git-scm.com/):

```
git clone https://github.com/evereux/pycatia-tools.git
```

Alternatively you can download a copy of the 
[zipped](https://github.com/evereux/pycatia-tools/archive/refs/heads/main.zip) 
archive. 

Change directory to the project folder and create a 
[virtual environment](https://docs.python.org/3/library/venv.html) for the 
project.

```
python -m venv env
```

Activate the virtual environment

```
env\Scripts\activate.bat
```

Install the requirements.

```
pip install -r requirements.txt
```

Running
-------

To run the application:

```
flask run
```
Open a web browser and access the url https://127.0.1:5578



Building
========

To build an executable do the following:

```
pip install nuitka
```

```
python -m nuitka --standalone --include-data-dir=<path_to>\pycatia-tools\application\templates=application/templates --include-data-dir=<path_to>\\pycatia-tools\application\static=application/static pycatia-tools-exe.py
```
