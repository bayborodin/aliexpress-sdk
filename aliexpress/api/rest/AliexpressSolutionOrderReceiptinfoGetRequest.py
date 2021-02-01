"""
Created by auto_sdk on 2019.08.22
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionOrderReceiptinfoGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param1 = None

    def getapiname(self):
        return "aliexpress.solution.order.receiptinfo.get"
