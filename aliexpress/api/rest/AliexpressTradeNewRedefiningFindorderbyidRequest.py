"""
Created by auto_sdk on 2020.03.12
"""
from aliexpress.api.base import RestApi


class AliexpressTradeNewRedefiningFindorderbyidRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param1 = None

    def getapiname(self):
        return "aliexpress.trade.new.redefining.findorderbyid"
