"""
Created by auto_sdk on 2019.11.26
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionFeedListGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.current_page = None
        self.feed_type = None
        self.page_size = None
        self.status = None

    def getapiname(self):
        return "aliexpress.solution.feed.list.get"
