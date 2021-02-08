"""
Created by auto_sdk on 2020.08.12
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionProductEditRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.edit_product_request = None

    def getapiname(self):
        return "aliexpress.solution.product.edit"
