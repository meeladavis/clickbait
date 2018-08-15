# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = 'C:\\Users\meela\Documents\dev\clickbait\clickdata.csv'

#TODO: Add dtype
clickdata =  pd.read_csv(filename,sep=',',skiprows=1, names = ['ID_ENTRY','ID_USER','ID_CONVERSATION','ID_EXPERIMENT','DATE_EVENT','FLAG_JAVA_ENABLED','TEXT_ACTION_DATA','TEXT_ACTION_TYPE','TEXT_APPLICATION_NAME','TEXT_APPLICATION_VERSIO','TEXT_EVENT_DATA','TEXT_EVENT_TYPE','TEXT_EXPERIMENT_VARIANT','TEXT_FLASH_VERSION','TEXT_IP_ADDRESS','TEXT_OPERATING_SYSTEM','TEXT_PROTOCOL_VERSION','TEXT_REFERRER','TEXT_SCREEN_NAME','TEXT_SCREEN_RESOLUTION','TEXT_URL','TEXT_USER_AGENT','TEXT_VIEW_PORT_SIZE'])
clickdata_np = np.array(clickdata)
#check that we have the right data
print("clickdata")
print(clickdata_np)

users = clickdata_np[:,1]
print("Total number of users: " + str(len(users)))
print(users)

sns.distplot( a=users, hist=True, kde=False, rug=False )
sns.plt.show()


#count of unique users from 'users' array
uniqueusers=list(dict.fromkeys(users))
print("Total number of unique users: " + str(len(uniqueusers)))

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
