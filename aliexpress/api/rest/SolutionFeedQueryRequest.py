"""
Created by auto_sdk on 2020.08.11
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionFeedQueryRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.job_id = None

    def getapiname(self):
        return "aliexpress.solution.feed.query"
