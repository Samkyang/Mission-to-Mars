#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[3]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[6]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[7]:


slide_elem.find('div', class_='content_title')


# In[8]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[9]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[10]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[14]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[15]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[16]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[17]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[23]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[24]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[25]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
# 3a. Cerberus
browser.visit(url)
browser.links.find_by_partial_text('Cerberus').click()
html = browser.html
cerberus_soup = soup(html, 'html.parser')
cerberus_url = cerberus_soup.select_one('div.downloads a').get("href")
cerberus_title = cerberus_soup.select_one('div.content h2').text

#dictionary:
cerberus_dict = {
        "img_url": cerberus_url,
        "title": cerberus_title
    }

hemisphere_image_urls.append(cerberus_dict)


# In[26]:


# 3b. Schiaparelli
browser.visit(url)
browser.links.find_by_partial_text('Schiaparelli').click()
html = browser.html
schiaparelli_soup = soup(html, 'html.parser')
schiaparelli_url = schiaparelli_soup.select_one('div.downloads a').get("href")
schiaparelli_title = schiaparelli_soup.select_one('div.content h2').text

#dictionary:
schiaparelli_dict = {
        "img_url": schiaparelli_url,
        "title": schiaparelli_title
    }

hemisphere_image_urls.append(schiaparelli_dict)


# In[27]:


# 3c. Syrtis
browser.visit(url)
browser.links.find_by_partial_text('Syrtis').click()
html = browser.html
syrtis_soup = soup(html, 'html.parser')
syrtis_url = syrtis_soup.select_one('div.downloads a').get("href")
syrtis_title = syrtis_soup.select_one('div.content h2').text

#dictionary:
syrtis_dict = {
        "img_url": syrtis_url,
        "title": syrtis_title
    }

hemisphere_image_urls.append(syrtis_dict)


# In[28]:


# 3d Valles
browser.visit(url)
browser.links.find_by_partial_text('Valles').click()
html = browser.html
valles_soup = soup(html, 'html.parser')
valles_url = valles_soup.select_one('div.downloads a').get("href")
valles_title = valles_soup.select_one('div.content h2').text

#dictionary:
valles_dict = {
        "img_url": valles_url,
        "title": valles_title
    }

hemisphere_image_urls.append(valles_dict)


# In[29]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[30]:


# 5. Quit the browser
browser.quit()


# In[ ]:




