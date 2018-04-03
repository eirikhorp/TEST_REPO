import pandas as pd
import numpy as np

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

df.to_csv('./test.csv', index=False, header=False)
