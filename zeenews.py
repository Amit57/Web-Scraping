
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver


def get_news_data(url):
    
    
    count = 0
    
    fw=open('News.txt','w') 
    chromedriver = '/Users/amit/Desktop/Masters/Semester 2/Web Analytics/NBA/chromedriver'

    driver = webdriver.Chrome(chromedriver)
    driver.get(url)

    SCROLL_PAUSE_TIME = 2

    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
             
        count = count + 1

        time.sleep(SCROLL_PAUSE_TIME)
        print("page scroll count "+str(count))
    
        if count == 20:
            break
        
    print("breaking")
    
    print("parsing...")
    
    soup = BeautifulSoup(driver.page_source,"lxml")
    article = soup.find('section', {'class':re.compile('maincontent')})
    
    
    for news in article.find_all("a"):
        
        if news.has_attr('href'):
            
            href = news.attrs['href']
            
            c1 = re.sub('http://zeenews.india.com/india/', ' ', str(href))
            c2 = re.sub('/india/', ' ', str(c1))
            c3 = re.sub('-', ' ', str(c2))
            c4 = re.sub('.html', ' ', str(c3))
            c5 = re.sub(r'[^a-zA-Z]', ' ', str(c4))
            fw.write(c5+'\n')
            

    
    fw.close()
    driver.quit()
    
    uniqlines = set(open('News.txt').readlines())

    op = open('Zee_News.txt', 'w')
    op.writelines(set(uniqlines))
    op.close()


    
    print("finished: Browser closed")
    



    
  
if __name__=='__main__':
    url='http://zeenews.india.com/india'
    get_news_data(url)
    