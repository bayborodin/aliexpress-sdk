"""
Created by auto_sdk on 2019.11.18
"""
from aliexpress.api.base import RestApi


class AliexpressTradeRedefiningFindorderbaseinfoRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param1 = None

    def getapiname(self):
        return "aliexpress.trade.redefining.findorderbaseinfo"
