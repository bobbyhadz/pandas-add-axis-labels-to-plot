# How to Add Axis Labels to a Plot in Pandas

import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'team_A': [1, 3, 6, 9, 12, 15],
    'team_B': [0, 1, 4, 7, 8, 9],
})

df.plot(xlabel='Match', ylabel='Points')

plt.show()