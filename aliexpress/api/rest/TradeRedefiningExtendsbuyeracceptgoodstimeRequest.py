"""
Created by auto_sdk on 2018.12.18
"""
from aliexpress.api.base import RestApi


class AliexpressTradeRedefiningExtendsbuyeracceptgoodstimeRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param0 = None
        self.param1 = None

    def getapiname(self):
        return "aliexpress.trade.redefining.extendsbuyeracceptgoodstime"
