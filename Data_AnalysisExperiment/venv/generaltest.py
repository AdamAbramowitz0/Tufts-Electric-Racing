import socket
import time
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.animation import FuncAnimation
import pandas as pd
from decimal import *
import threading

lock = threading.Lock()



#USER SETS THE FOLLOWING
sensors = ["TemperatureRR","Moisture","Wheel Speed"]
frequencyHz = [10,1,10]
largestFreq = 10