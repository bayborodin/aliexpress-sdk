"""
Created by auto_sdk on 2018.07.25
"""
from aliexpress.api.base import RestApi


class AliexpressPostproductRedefiningGetsizechartinfobycategoryidRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.category_id = None

    def getapiname(self):
        return "aliexpress.postproduct.redefining.getsizechartinfobycategoryid"
