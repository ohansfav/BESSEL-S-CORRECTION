#import pandas as pd
import numpy as np

data = [1,2,3,4,5]


#cal the standard deviation using pandas
df = pd.DataFrame(data)
float(df.std())


#using numpy
arr = np.array(data)
np.std(arr)
