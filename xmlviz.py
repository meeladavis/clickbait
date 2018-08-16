import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


filename = '/Users/meeladavis/PycharmProjects/clickbait/xmldata.csv'

types = {'Lines': float, 'Words': float, 'Characters' : float, 'File' : str}

xml_length_data = pd.read_csv(filename,sep=',',nrows=49,skiprows=1, names = ['Lines','Words', 'Characters', 'File'], dtype=types)
xml_length_data_np = np.array(xml_length_data)
#check that we have the right data
#print("data")
#print(xml_length_data_np)
#print("data2")
#print(xml_length_data_np[:,0]


#Create am array with my other data
#CmX = 34 lines / 1262 characters; JS =  lines / 389 chars

#Do a plot with the data
RealExample_np = np.array([[34,35], [1262,389]], dtype=np.int64)
RE_words = RealExample_np[0,:]
RE_chars = RealExample_np[1,:]
print(RealExample_np)
print(RE_chars)
print(RE_words)


sns.catplot(data=RE_chars,kind='count', y=None, x=None)
plt.show()