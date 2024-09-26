import scrapy
import json
from lxml import etree
from ..items import BossItem

class BossspiderSpider(scrapy.Spider):
    name = "Bossspider"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["http://www.zhipin.com/"]
    
    json_url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101020100&page={}"

    def start_request(self):
        for i in range(1, 10):
            url = self.json_url.format(i)
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        res = json.loads(response.text)
        for job in res['data']['zpData']['jobList']:
            item = BossItem()
            item['job_name'] = job['jobName']
            item['job_salary'] = job["salaryDesc"]
            item['experience'] = job["jobExperience"]
            item['degree'] = job['jobDegree']
            item['company_name'] = job['brandName']
            item['city'] = job['cityName']
            item['area'] = job['areaDistrict']
            skills = ''
            for i in job['skills']:
                skills += i
                skills += '\n'
            item['job_skills'] = skills

            yield item
