import numpy as np
import pandas as pd
from pylinkparse import Raw

path = 'pylinkparse/tests/data/'
fname = path + 'test_raw.asc'

raw = Raw(fname)

print raw