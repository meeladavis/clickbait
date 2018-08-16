# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#filename = 'C:\\Users\meela\Documents\dev\clickbait\clickdata.csv'
filename = '/Users/meeladavis/Python/pythonscripts/cb/clickdata.csv'


#TODO: Add dtype
clickdata =  pd.read_csv(filename,sep=',',skiprows=1, names = ['ID_ENTRY','ID_USER','ID_CONVERSATION','ID_EXPERIMENT','DATE_EVENT','FLAG_JAVA_ENABLED','TEXT_ACTION_DATA','TEXT_ACTION_TYPE','TEXT_APPLICATION_NAME','TEXT_APPLICATION_VERSIO','TEXT_EVENT_DATA','TEXT_EVENT_TYPE','TEXT_EXPERIMENT_VARIANT','TEXT_FLASH_VERSION','TEXT_IP_ADDRESS','TEXT_OPERATING_SYSTEM','TEXT_PROTOCOL_VERSION','TEXT_REFERRER','TEXT_SCREEN_NAME','TEXT_SCREEN_RESOLUTION','TEXT_URL','TEXT_USER_AGENT','TEXT_VIEW_PORT_SIZE'])
clickdata_np = np.array(clickdata)
#check that we have the right data
print("clickdata")
print(clickdata_np)

users = clickdata_np[:,1]
print("Total number of users: " + str(len(users)))
print(users)


#clean the uA from the users before doing a distplot (so that we have floats)
i=0
cleanusers = np.array(users)
cleanusers_db = np.array(users)

for user in users:
    cleanusers[i] = user[2:]
    cleanusers_db[i] = user[:2]
#    print(user)
#    print(cleanusers[i])
#    print(cleanusers_db[i])
    i = i + 1

print("Total number of 'clean' users: " + str(len(cleanusers)))
print(cleanusers_db)
sns.distplot(cleanusers_db)

#violin plot
#sns.violinplot(data=users)
#plt.show()

#violin plot, single data point

#sns.catplot('myplot', data=users, kind='count')
#plt.show()


#Distribution / histogram plot
#sns.distplot( cleanusers )
#sns.plt.show()


#count of unique users from 'users' array
uniqueusers=list(dict.fromkeys(users))
print("Total number of unique users: " + str(len(uniqueusers)))



#Number of datasets

unique_dbs=list(dict.fromkeys(cleanusers_db))
print("Total number of unique datasets: " + str(len(unique_dbs)))
#cleanusers_db_freq = np.array(pd.Series(cleanusers_db).value_counts())
#print(cleanusers_db_freq)

from collections import Counter
db_count = np.array(Counter(cleanusers_db))
print(db_count)


#catplot
sns.catplot(data=cleanusers_db_freq)
plt.show()

#Browser / OS
#browser_moz =
#browser_saf
#browser_ie
#OS_win
#OS_osx
#OS_ios

#ScreenRes
#Let's try a scatter plot with Screen res
## Change color with c and alpha. I map the color to the X axis value.
#plt.scatter(x, y, s=z*2000, c=x, cmap="Blues", alpha=0.4, edgecolors="grey", linewidth=2)
