"""
Created by auto_sdk on 2020.09.08
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionOrderInfoGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param1 = None

    def getapiname(self):
        return "aliexpress.solution.order.info.get"
