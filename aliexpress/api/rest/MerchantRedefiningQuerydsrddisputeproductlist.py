from aliexpress.api.base import RestApi


class MerchantRedefiningQuerydsrddisputeproductlistRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param1 = None

    def getapiname(self):
        return 'aliexpress.merchant.redefining.querydsrddisputeproductlist'
