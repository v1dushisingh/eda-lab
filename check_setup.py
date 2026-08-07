import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
print("Python, Version :", sys.version.split()[0])
print("numpy, Version :", np.__version__)
print("pandas Version :", pd.__version__)
print("matplotlib Version :", matplotlib.__version__)
print("25EC01053")

# a one-line smoke test of the plotting back-end
plt.plot([0, 1, 2, 3], [0, 1, 4, 9], marker="o")
plt.title("If you can see this window, the setup works")

plt.xlabel("x"); plt.ylabel("Drain Current,I_D(mA)")

plt.grid(True)
plt.show()
