"""
Created by auto_sdk on 2019.06.20
"""
from aliexpress.api.base import RestApi


class AliexpressPostproductRedefiningQueryproductgroupidbyproductidRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.product_id = None

    def getapiname(self):
        return "aliexpress.postproduct.redefining.queryproductgroupidbyproductid"