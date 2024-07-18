import random
import numpy as np
import pandas as pd
index = "none"
assigned = "NULL"

# first a perosn gets an index then they will
# be assigned a line from the text, then the line will be appended 
df= pd.read_csv ("helo.txt")
print(df)
index = input ("enter your index ")


integer_location = np.where(df.index == 3454)[0]
start = max(0, integer_location - 55)
end = max(1, integer_location)
dfRange = df.iloc[start:end]

assigned = random.randint(dfRange,dfRange)

print(assigned)


