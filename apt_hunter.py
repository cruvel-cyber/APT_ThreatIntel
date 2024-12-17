import scrapy
import re
import requests
from bs4 import BeautifulSoup

class AptZeroDayCrawler(scrapy.Spider):
    name = "apt_zero_day"
    start_urls = [
        "https://www.cisa.gov/news",
        "https://www.fireeye.com/blog.html",
        "https://www.bleepingcomputer.com/",
        "https://www.securityfocus.com/",
        "https://www.exploit-db.com/",
        "https://www.mitre.org/",
        "https://www.cybersecurity-news.com/",
        "https://www.darkreading.com/"
    ]
    
    def parse(self, response):
        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # Example keywords for detecting APT or Zero-day references
        keywords = ['APT', 'zero-day', 'exploit', 'vulnerability', 'CVE', 'malware', 'CISA', 'Hacker', 'CVE', 'cyberattack']
        
        # Look for relevant links or text in the page
        for article in soup.find_all('a', href=True):
            link = article['href']
            text = article.get_text().lower()
            
            # If article text matches keywords, check the article
            if any(keyword.lower() in text for keyword in keywords):
                yield {
                    'title': article.get_text(),
                    'link': link,
                    'summary': text
                }
                
        # Follow pagination links to continue scraping
        next_page = soup.find('a', {'class': 'next'})
        if next_page:
            next_url = next_page.get('href')
            yield response.follow(next_url, self.parse)
