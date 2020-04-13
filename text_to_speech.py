#!/usr/bin/env python
# coding: utf-8

# # Text to voice Converter

# There are several APIs available to convert text to speech in python. 
# One of such APIs is the Google Text to Speech API commonly known as the gTTS API. 
# gTTS is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file.
# 
# The gTTS API supports several languages including English, Hindi, Tamil, French, German and many more. 
# The speech can be delivered in any one of the two available audio speeds, fast or slow. 
# However, as of the latest update, it is not possible to change the voice of the generated audio.

# ## Applications :-

# 1. Helpful for Blind person
# 2. Useful at railway stations for the announcements
# 3. Useful in Mobile communications 
# 4. Useful for the people who can't speak 
# --- and much more 

# ## Let's begin the code 

# In[15]:


#importing the required pakages 

from gtts import gTTS 
import os


# In[16]:


#reading the files

with open('hindi_story.txt', 'r',encoding="utf8") as myfile:
    hindi_story = myfile.read()

with open('eng_story.txt', 'r',encoding="utf8") as myfile:
    eng_story = myfile.read()

with open('metro.txt', 'r',encoding="utf8") as myfile:
    metro = myfile.read()


# In[17]:


#creating gTTS object

hs_obj = gTTS(text=hindi_story, lang='hi', slow=False) 
es_obj = gTTS(text=eng_story, lang='en', slow=False) 
m_obj = gTTS(text=metro, lang='hi', slow=False) 


# In[18]:


#converting gTTS object to mp3 files 

hs_obj.save("hindi.mp3")
es_obj.save("english.mp3")
m_obj.save("metro.mp3")

#Now we play these files 


# In[19]:


os.system("hindi.mp3") 


# In[20]:


os.system("english.mp3") 


# In[21]:


os.system("metro.mp3") 


# In[ ]:




