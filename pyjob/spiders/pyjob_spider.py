# -*- coding: utf-8 -*-
import scrapy

from pyjob.items import PyjobItem


class PyjobSpider(scrapy.Spider):
    name = 'pyjob_spider'
    allowed_domains = ['python.org']
    start_urls = ['https://www.python.org/jobs/']

    def parse(self, response):
        # `ol.list-recent-jobs`内の`li`アイテムを全取得
        list_recent_jobs = response.css('ol.list-recent-jobs li')

        for jobs in list_recent_jobs:
            item = PyjobItem()

            # タイトル: `.listing-company-name`内の`a`のテキスト
            item['title'] = jobs.css('.listing-company-name a::text').extract_first()

            # 社名: `.listing-company-name`内のテキスト群を全結合し、`strip()`で空白文字を全消去
            item['company'] = "".join(jobs.css('.listing-company-name::text').extract()).strip()

            # 勤務場所: `.listing-location`内の`a`のテキスト
            item['location'] = jobs.css(".listing-location a::text").extract_first()

            yield item

        # `NEXT`ボタンの`a`の`href`属性を取得、遷移先があればそれを投げる
        next_href = response.css('li.next a::attr(href)').extract_first()
        if next_href:
            joined_next_url = response.urljoin(next_href)
            yield scrapy.Request(joined_next_url, callback=self.parse)
