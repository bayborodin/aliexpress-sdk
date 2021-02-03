"""
Created by auto_sdk on 2020.02.11
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionBatchProductDeleteRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.product_ids = None

    def getapiname(self):
        return "aliexpress.solution.batch.product.delete"
