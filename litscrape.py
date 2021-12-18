#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url= "https://www.literotica.com/s/oops-sorry-dean-flashes-wife-1"


# In[3]:


url = input ("Type literotica story url \nurl example - https://www.literotica.com/s/oops-sorry-dean-flashes-wife-1 \nType URL:")


# In[4]:


try:    
    storyhtml = requests.get(url,headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    print('story found')
    soup = BeautifulSoup(storyhtml.content, "lxml")
except e:
    import traceback
    traceback.print_exc()


# In[5]:


fname= url.split("/s/")[-1] +".txt"
fname


# In[6]:


lastpage=0
try:
    for pagedesc in soup.select('div[class*="panel clearfix"]'):
        x = pagedesc.find_all("a")

        for page in x:
            lpstr = page.attrs['href']    
            if "page=" in lpstr:
                lastpage = int(lpstr.split("page=")[1])
#         print(lastpage)
except:
    import traceback
    traceback.print_exc()


# In[7]:


lastpage


# In[8]:


pages_to_fetch = []
pages_to_fetch.append(url)
for p in range(2, lastpage+1):        
    if lastpage!=0:
        tempurl = url + "?page=" + str(p)
        pages_to_fetch.append(tempurl)


# In[9]:


pages_to_fetch


# In[10]:


def fetchpage(url):
    story = "ERROR!!!"
    try:       
        storyhtml = requests.get(url,headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
        print('fetching data from: ', url)
        soup = BeautifulSoup(storyhtml.content, "lxml")
        
        for storypart in soup.select('div[class*="panel article"]'):
            data = storypart.find_all('p')
            story = "\n\n".join([p1.text for p1 in data])
    except e:
        import traceback
        traceback.print_exc()

    return story
    


# In[17]:


import time
fullstory = fname.split(".txt")[0]
for page in pages_to_fetch:
    story = fetchpage(page)
#     time.sleep(1)
    fullstory = fullstory + "\n\nSource:" + page + "\n\n" + story + "\n" 


# In[18]:


with open(fname, 'w', encoding="utf-8") as f:
    f.write(fullstory)
    print("Story exported as :", fname)

# In[ ]:




