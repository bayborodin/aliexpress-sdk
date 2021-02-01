"""
Created by auto_sdk on 2019.06.11
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionProductListGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.aeop_a_e_product_list_query = None

    def getapiname(self):
        return "aliexpress.solution.product.list.get"
