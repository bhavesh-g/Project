# -*- coding: utf-8 -*-
# Author: Bhavesh Gupta
# Email: guptabhavesh6@gmail.com
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json
import os

# This function separates the protocol and domain name from URL and also checks for www to be not present in URL.
# Returns a list with two elements, first being protocol and other one is domain name.
def make_urls(url):
        if(('http' in url or 'https' in url) and 'www' not in url and len(url)>10):
            final_urls= url.split('://')
            return final_urls
        else:
            return False
        


class WikiSpider(CrawlSpider):

    final_urls=False
    flag=0
    print('''
------------------------------------------------------------------------------------------------------------------------

* Welcome to TextExtractor !!!

* This is a tool to extract all the <p> tags text from each webpage of given website.

* You will need to enter the Website URL.

* Make sure your last command must be 'scrapy crawl extrator' (without quotes).

Example starting URL:

http://newsonair.com

or

https://doercity.com

------------------------------------------------------------------------------------------------------------------------''')
    while(final_urls==False):
        if(flag>0):
            print("\n\n***************Please check input URL format and try again!! Remove the 'www' from URL if present***************\n\n")
        url=input("\n\nEnter the starting URL, !!! Make sure to not add 'www' !!!\n\n:")
        final_urls= make_urls(url)
        flag+=1

# This checks for a 'output.json' named file in same directory, if already present, clears its content.
    if('data' in os.listdir() ):
            
            with open('data/output.json','w') as fp:
                    pass
    else:
            os.mkdir('data')
            with open('data/output.json','w') as fp:
                    pass
    
        
    name = 'extractor'
    allowed_domains=[final_urls[1],url.split('/')[2]]
    start_urls= (url,)
    rules=  (Rule(LinkExtractor(allowed_domains),callback='parse_page',follow=True),) 
    
    def parse_page(self, response):
        try:
                
                if(response.status==200):
                        paragraph_list=response.xpath('//p/text()').extract()
                        final= []
                        l=len(paragraph_list)
            
# To clean the paragraph text from trailing whitespaces or new line .

                        for i in range(l):
                                paragraph_list[i]= paragraph_list[i].strip()
                                if(paragraph_list[i]!= ''):
                                        final.append(paragraph_list[i])
                
                        paragraph_list= " ".join(final)

            
                        yield {
                        'page':response.url,

                        'content':paragraph_list.replace('\n',' ').replace('\r',' ')
                              }
        except:
                pass
            
    def close(self,reason):
            
        try:
                
                with open('data/output.json','r') as fp:
                
                        json_list= json.load(fp)
                        wrapper={}
                        wrapper["pages"]= json_list
        
                with open('data/output.json','w') as fp:

                        json.dump(wrapper,fp)
                        fp.close()
        except:
                pass

        
    
            
            
        






       
       
