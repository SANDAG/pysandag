[![Coverage Status](https://coveralls.io/repos/github/SANDAG/pysandag/badge.svg?branch=master)](https://coveralls.io/github/SANDAG/pysandag?branch=master)
[![Build Status](https://travis-ci.org/SANDAG/pysandag.svg?branch=master)](https://travis-ci.org/SANDAG/pysandag)

# pysandag

pysandag is a utility package containing commonly used classes and methods that are used across
 a broad range of projects at SANDAG.

## Installation
The installation uses the standard python setuptools package. To install this package download the pacakage and simply run:

*python.exe setup.py install*  
 --or--  
 *https://github.com/SANDAG/pysandag/blob/master/db.yml*  
   
## Methods
```python
from pysandag.database import get_connection_string(cfg_file, cfg_section)
```

```python
from pysandag.gis import transform_wkt(geom_wkt)
```