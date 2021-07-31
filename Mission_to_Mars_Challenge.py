#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import datetime as dt
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set up splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first <a> tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[8]:


# Scrape the title
title = news_soup.find('h2').text
title


# ### Featured Images

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[14]:


# use Pandas 'read_html' function to scrape the facts table into a dataframe
df = pd.read_html('https://galaxyfacts-mars.com')[0]    
# Assign columns and set index of dataframe but remove the print statements now that we know this code is working
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[15]:


# Convert dataframe into HTML format using the Pandas .to_html function, add bootstrap
df.to_html()


# In[16]:


# End automated browsing session
browser.quit()


# In[17]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[18]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[19]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[20]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[21]:


slide_elem.find('div', class_='content_title')


# In[22]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[23]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[24]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[25]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[26]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[27]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[28]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[29]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[30]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[31]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[32]:


# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
browser.visit(url)


# In[33]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
links = browser.find_by_css('a.product-item img')
print(len(links))
print(links.first)


# In[34]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(len(links)):
    hemisphere_dict = {}
    browser.find_by_css('a.product-item img')[i].click()
    sample_img = browser.links.find_by_text('Sample').first
    print(sample_img['href'])
    hemisphere_dict['url'] = sample_img['href']
    hemisphere_dict['title'] = browser.find_by_css('h2.title').text
    
    
    
    
    hemisphere_image_urls.append(hemisphere_dict)
    browser.back()
    


# In[35]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[36]:


# 5. Quit the browser
browser.quit()

