from aliexpress.api.base import RestApi


class PostproductRedefiningClaimtaobaoproductsapiRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.url = None

    def getapiname(self):
        return 'postproduct.redefining.claimtaobaoproductsapi'
