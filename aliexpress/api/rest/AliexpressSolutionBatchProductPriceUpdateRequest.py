"""
Created by auto_sdk on 2019.12.11
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionBatchProductPriceUpdateRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.mutiple_product_update_list = None

    def getapiname(self):
        return "aliexpress.solution.batch.product.price.update"
