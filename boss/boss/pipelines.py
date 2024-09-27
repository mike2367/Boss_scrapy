# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class BossPipeline:
    def process_item(self, item, spider):
        return item

class mysqlPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='boss',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = """
            INSERT INTO jobs (
                job_name, job_salary, experience, degree, 
                company_name, city, area, job_skills
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            item['job_name'],
            item['job_salary'],
            item['experience'],
            item['degree'],
            item['company_name'],
            item['city'],
            item['area'],
            item['job_skills']
        )
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print('save data', item['job_name'], 'to mysql successfully')
        except Exception as e:
            print('save data', item['job_name'], 'to mysql failed', e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
