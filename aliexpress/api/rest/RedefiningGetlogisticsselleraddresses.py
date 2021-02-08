"""
Created by auto_sdk on 2018.07.25
"""
from aliexpress.api.base import RestApi


class AliexpressLogisticsRedefiningGetlogisticsselleraddressesRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.seller_address_query = None

    def getapiname(self):
        return "aliexpress.logistics.redefining.getlogisticsselleraddresses"
