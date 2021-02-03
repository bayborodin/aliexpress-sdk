"""
Created by auto_sdk on 2020.09.08
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionOrderGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param0 = None

    def getapiname(self):
        return "aliexpress.solution.order.get"
