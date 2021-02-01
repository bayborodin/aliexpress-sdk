"""
Created by auto_sdk on 2019.05.10
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionSchemaProductInstancePostRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.product_instance_request = None

    def getapiname(self):
        return "aliexpress.solution.schema.product.instance.post"
