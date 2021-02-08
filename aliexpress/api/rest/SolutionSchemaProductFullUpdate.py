"""
Created by auto_sdk on 2019.07.10
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionSchemaProductFullUpdateRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.schema_full_update_request = None

    def getapiname(self):
        return "aliexpress.solution.schema.product.full.update"
