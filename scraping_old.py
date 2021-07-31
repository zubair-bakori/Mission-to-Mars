# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import datetime as dt
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager



def main():

    # Set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    news_title, news_p = mars_news_title(browser)
     

    data = {
        'news_title': news_title,
        'news_paragraph': news_p,
        'img_feature': get_image_feature(browser)
    
    
   
    
    
    }

    browser.quit()
    return data

def mars_news_title(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Set up the HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')

    slide_elem.find('div', class_='content_title')

    # Use the parent element to find the first <a> tag and save it as 'news_title'
    news_title = slide_elem.find('div', class_='content_title').get_text()
    
    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    # Scrape the title
    #title = news_soup.find('h2').text
    return news_title, news_p

def get_image_feature(browser):


    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    # Use base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    return img_url



# use Pandas 'read_html' function to scrape the facts table into a dataframe
df = pd.read_html('https://galaxyfacts-mars.com')[0]    
# Assign columns and set index of dataframe but remove the print statements now that we know this code is working
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Convert dataframe into HTML format using the Pandas .to_html function, add bootstrap
df.to_html()

# End automated browsing session

if __name__ == '__main__':
    print(main())
    