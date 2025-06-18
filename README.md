should probably change to using it in a way so that you can just pass the object, and this module can change the characteristics, instead of actually drawing the chart, so that we can future proof and least maintain this project. 

# kptgraphs

My python module for me to use my own standardized graphs.

## Installation

To install this in your python environment, run the following command:

1. Activate your environment

2. Clone this repository

```bash
git clone https://github.com/KrishnarajT/kptgraphs
```
3. Change directory to the cloned repository

```bash
cd kptgraphs
```

4. Pip install the module

```bash
pip install .
```

5. Import the module in your python script

```python
import kptgraphs
```

## Usage

```python

from kptgraphs.basic_graphs import BasicGraphs

# Create an object of BasicGraphs
bg = BasicGraphs()
bg.test()
```
