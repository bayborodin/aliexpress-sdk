"""
Created by auto_sdk on 2019.04.08
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionSkuAttributeQueryRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.query_sku_attribute_info_request = None

    def getapiname(self):
        return "aliexpress.solution.sku.attribute.query"
