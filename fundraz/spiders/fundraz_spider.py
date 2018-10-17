import scrapy
from fundraz.items import FundrazItem
from datetime import datetime
import re

class FundrazSpider(scrapy.Spider):
	name = "fundraz_spider"
	start_urls = ["https://fundrazr.com/find"]                                                                                                                                                                                                    

	def parse(self,response):
		result_urls = response.xpath('//div[@id="campaign-nav-col"]//li/a/@href').extract()[6:] #extracting category hyperlink
		for url in result_urls: #iterating over category links
			yield scrapy.Request(url=url, callback=self.parse_result_page)
	def parse_result_page(self,response):
		category = response.xpath('//div[@id="title-panel"]/h1').extract() #xpath for title of category
		pages = [response.url + "&page=" + str(i) for i in range(1,11)] #list comprehension that iterates over each next page for a constant of 10 pages
		for page in pages:
			yield scrapy.Request(url=page, callback = self.parse_each_page, meta = {'category': category}) #category title for each loop
	def parse_each_page(self,response):
		category = response.meta['category']
		for href in response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"): #hyperlink for each campaign in each category
			url  = "https:" + href.extract() #adding https to hyperlink
			yield scrapy.Request(url=url, callback = self.parse_detail_page, meta = {'category': category})
	def parse_detail_page(self,response):
		item = FundrazItem()
		item['title']=  response.xpath("//div[contains(@id, 'campaign-title')]/descendant::text()").extract_first().strip() #title of campaign stripped into string format
		item['target']= ''.join(response.xpath('//div[@id="campaign-stats"]/div[1]/span[3]/text()').extract()).strip() #target amount for campaign stripped and joined into string format
		item['amountraised']= ''.join(response.xpath('//div[@id="campaign-stats"]/div[1]/span[1]/span[2]/text()').extract()).strip() #amount raised for campaign stripped and joined into string format
		item['numbercontributors']= int(response.xpath("//div[contains(@class, 'stats-secondary with-goal')]//span[contains(@class, 'donation-count stat')]/text()").extract_first()) #number of contributors taken in integer form
		item['currencyused']= ''.join(response.xpath("//div[contains(@class, 'stats-primary with-goal')]/@title").extract()).strip() #currency used stripped and joined into string format
		item['startDate']=''.join(response.xpath('//div[@id="launch-time-tooltip"]/div/p/span/text()').extract()).strip() #startDate for campaign stripped and joined into string format
		item['category'] = response.meta['category'] #category xpath taken from above

		yield item
		