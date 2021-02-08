"""
Created by auto_sdk on 2019.10.08
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionMerchantProfileGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)

    def getapiname(self):
        return "aliexpress.solution.merchant.profile.get"
