#!/usr/bin/env python
# coding: utf-8

# In[24]:


import requests
from bs4 import BeautifulSoup
import time

# GEL - pass url via command line and skip existing files
import sys
import os
if sys.argv[1]:
    authurl=sys.argv[1];
else:

    # In[25]:


    authurl = "https://www.literotica.com/stories/memberpage.php?uid=1253141&page=submissions"


    # In[26]:


    authurl = input ("Type literotica author story submissions url \nurl example - https://www.literotica.com/stories/memberpage.php?uid=1253141&page=submissions \nType URL:")


# In[27]:



try:
    authpagehtml = requests.get(authurl,headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    print('auth found')
    authsoup = BeautifulSoup(authpagehtml.content, "lxml")
except:
    import traceback
    traceback.print_exc()


# In[28]:


rootstories =[]
seriesstories = []
try:
    for pagedesc in authsoup.select('a[class*="contactheader"]'):
        author = pagedesc.text
except:
    import traceback
    traceback.print_exc()

try:
    for pagedesc in authsoup.select('tr[class*="root-story"]'):
        x = pagedesc.find_all("a")

        for page in x:
            lpstr = page.attrs['href']
            if "/s/" in lpstr:
               rootstories.append(lpstr)
except:
    import traceback
    traceback.print_exc()

try:
    for pagedesc in authsoup.select('tr[class*="sl"]'):
        x = pagedesc.find_all("a")

        for page in x:
            lpstr = page.attrs['href']
            if "/s/" in lpstr:
               seriesstories.append(lpstr)
except:
    import traceback
    traceback.print_exc()


# In[29]:


allstories = rootstories + seriesstories
print( "stories to extract=> ",allstories)


# In[30]:


def extractStory(author,url):
    import os
    os.makedirs(author,exist_ok=True)
    try:
        storyhtml = requests.get(url,headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
        print('story found')
        soup = BeautifulSoup(storyhtml.content, "lxml")
    except e:
        import traceback
        traceback.print_exc()


    fname= url.split("/s/")[-1] +".txt"
    fname

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

    lastpage

    pages_to_fetch = []
    pages_to_fetch.append(url)
    for p in range(2, lastpage+1):
        if lastpage!=0:
            tempurl = url + "?page=" + str(p)
            pages_to_fetch.append(tempurl)

    pages_to_fetch

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


    import time
    fullfilename = author +"/" + fname

    # GEL - check to see if the fullfilename already exists and skip if we already have it
    if os.path.exists(fullfilename):
        print (fullfilename+" already exists, skipping \n");
    else:
        fullstory = fname.split(".txt")[0]
        for page in pages_to_fetch:
            story = fetchpage(page)
        #     time.sleep(1)
            fullstory = fullstory + "\n\nSource:" + page + "\n\n" + story + "\n"

        with open(fullfilename, 'w', encoding="utf-8") as f:
            f.write(fullstory)
            print("Story exported as :", fullfilename)


# In[31]:


for url in allstories:
    try:
        print("----------------")
        print("Extracting story=> ", url)
        extractStory(author,url)
        print("----------------")
    except:
        import traceback
        traceback.print_exc()

