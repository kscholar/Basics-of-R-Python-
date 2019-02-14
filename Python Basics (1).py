#This python code is regardingthe basics of python programming
# coding: utf-8

# In[52]:


#Setting the Working Directory
import os
os.chdir("D:/python & R/Kkamaljeet Singh (Data Scientist1)/Assignment")


# In[53]:


#Checking the Set Working DIrectory
os.getcwd()


# In[72]:


#loading the CSV File in Python by skipping the 2nd row
import pandas as pd
data = pd.read_csv("IMDB_data.csv",encoding='latin-1',skiprows=[2])
data


# In[71]:


#Extracting the the unGenres and its count and storing it in the data frame with Index Key 
d1=data["Genre"].unique()
d2=data["Genre"].nunique()
genre_df=data["Genre"].value_counts().to_frame().reset_index().rename(columns={"index":"index","Genre":"count"})


# In[57]:


#Checking the New DataFrame 
genre_df


# In[58]:


#Sorting the Dataframe in ascending order of Genre
Varasc=data.sort_values("Genre",ascending=True)


# In[59]:


Varasc


# In[60]:


#Converting the required datatypes
Varasc['imdbVotes'] = pd.to_numeric(Varasc['imdbVotes'],errors='coerce')
Varasc['imdbRating'] = pd.to_numeric(Varasc['imdbRating'],errors='coerce')


# In[61]:


#checking the dataFrame
Varasc


# In[62]:


# creating the new Variable in the existing DataFrame
import numpy as np
newvar=Varasc.imdbVotes-Varasc.imdbRating
diff= newvar*newvar
Varasc['Difference']= diff


# In[63]:


Varasc


# In[65]:


Varasc.to_csv("IMDB_DATA output in python.csv",index= False )
os.getcwd()

