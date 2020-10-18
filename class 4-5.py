#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from nltk.corpus import stopwords


# In[3]:


def gender_features(word):
    return{'last_letter':word[-1]}


# In[4]:


from nltk.corpus import names


# In[5]:


names.words()


# In[6]:


len(names.words())


# In[7]:


labeled_names = [(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')]


# In[8]:


labeled_names


# In[9]:


import random
random.shuffle(labeled_names)


# In[10]:


labeled_names


# In[11]:


featureset = [(gender_features(n),gender) for (n,gender) in labeled_names]


# In[12]:


featureset


# In[13]:


train_set,test_set = featureset[:5500],featureset[5501:]


# In[14]:


test_set


# In[17]:


import nltk
classifier = nltk.NaiveBayesClassifier.train(train_set)


# In[19]:


nltk.classify.accuracy(classifier,test_set)


# In[20]:


from sklearn.feature_extraction.text import CountVectorizer


# In[21]:


vect = CountVectorizer(binary=True)


# In[22]:


corpus =  ["Tessaract is good optical character recognition engine  ", "optical character recognition is significant "]


# In[23]:


vect.fit(corpus)


# In[24]:


vocab = vect.vocabulary_


# In[25]:



vocab


# In[26]:


vect.transform(["This is a good optical illusion."]).toarray()


# In[27]:



from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform(["Google Cloud Vision is a character recognition engine"]).toarray(), vect.transform(["OCR is an optical character recognition engine"]).toarray())
print(similarity)


# In[ ]:




