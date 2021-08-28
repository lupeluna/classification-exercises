import pandas as pd
import numpy as np
import os

#visualize
import seaborn as sns
import matplotlib.pyplot as plt

#acquire
from env import host, user, password
from pydataset import data

explore_univariate(train, cat_vars, quant_vars)