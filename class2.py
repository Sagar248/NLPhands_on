#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:



from nltk.corpus import stopwords
stopwords.words('English')


# In[3]:


stopwords.words('German')


# In[6]:


#not available in mother tongue - hindi


# In[7]:


entries = nltk.corpus.cmudict.entries()


# In[8]:


len(entries)


# In[9]:


from nltk.corpus import wordnet as wn


# In[10]:


wn.synsets('motorcar')


# In[11]:


wn.synsets('good')


# In[12]:


wn.synset('effective.s.04').lemma_names()


# In[13]:


from nltk.stem import LancasterStemmer


# In[17]:


lanc = LancasterStemmer()


# In[18]:


lanc.stem('sorryful')


# In[19]:


from nltk.stem import SnowballStemmer


# In[23]:


len(SnowballStemmer.languages)


# In[24]:


from nltk.stem import WordNetLemmatizer


# In[25]:


lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('radii'))


# In[26]:


lemmatizer.lemmatize('better', pos = 'a' )


# In[27]:


lemmatizer.lemmatize('am', pos = 'v' )


# In[28]:


pip install jieba


# In[ ]:




