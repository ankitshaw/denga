# DenGa
![](https://github.com/ankitshaw/denga/workflows/Build/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Data Augmentation for NLP Dataset using Thesaurus. 

It is still in work in progress mode and experimental in nature.

⛔ [NOT MAINTAINED] This repository is no longer maintained.

## Installation
Package can be installed like any other Python library, using (a recent version of) the Python package manager `pip`, on Linux, macOS, and Windows:
```
pip install -i https://test.pypi.org/simple/ denga
```
or, to update your installed version to the latest release:
```
pip install -i https://test.pypi.org/simple/ -U denga
```

## Example usage
```Python
from denga.genda import Genda

dataset = Genda("dataset.csv")       #Load Dataset

dataset.generate()                   #Generate the new dataset.

dataset.save()                       #Save the geneated dataset 
```

P.S: No queries to be entertained about the words denga or genda :P .
