from aliexpress.api.base import RestApi


class AliexpressPostproductRedefiningClaimtaobaoproductsapiRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.url = None

    def getapiname(self):
        return "aliexpress.postproduct.redefining.claimtaobaoproductsapi"
