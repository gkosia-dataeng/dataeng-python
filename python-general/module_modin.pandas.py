from modin import pandas as pd

# pandas operate on single core, modin distribute the data accross all the cores of the machine
# modin can handle daa larger than the memory
# modin implement all pandas dataframe so we need to change only the import statement