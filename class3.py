#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
text1 = '''A thing of beauty is a joy for ever:
Its loveliness increases; it will never
Pass into nothingness; but still will keep
All lovely tales that we have heard or read:
An endless fountain of immortal drink,
Pouring unto us from the heaven's brink.'''
for text in text1:
    sentences = nltk.sent_tokenize(text1)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        print(tagged)


# In[2]:



from nltk.tokenize import TweetTokenizer
text = 'Who did this? LOL'
tt = TweetTokenizer()
tt.tokenize(text)


# In[3]:


from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
type(raw)
len(raw)
raw[:75]
from nltk.tokenize import word_tokenize
tokens = word_tokenize(raw)
type(tokens)


# In[5]:


raw[:75]


# In[ ]:




