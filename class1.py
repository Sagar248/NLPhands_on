#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.corpus import brown


# In[3]:


brown.categories()


# In[4]:


brown.words(categories='humor')[0:50]


# In[5]:


from nltk.corpus import inaugural


# In[6]:


inaugural.fileids()


# In[7]:


inaugural.words(fileids ='2017-Trump.txt')[0:10]


# In[8]:


from nltk.probability import ConditionalFreqDist


# In[9]:


txt = inaugural.words(fileids ='2017-Trump.txt')[0:50]


# In[12]:


from nltk.probability import ConditionalFreqDist


# In[13]:


txt = inaugural.words(fileids ='2017-Trump.txt')[0:100]


# In[15]:


cfdi = ConditionalFreqDist((len(word), word) for word in txt)
cfdi[5]


# In[16]:


from nltk.corpus import webtext


# In[17]:


webtext.fileids()


# In[23]:


webtext.words(fileids ='pirates.txt')[0:10]


# In[ ]:




