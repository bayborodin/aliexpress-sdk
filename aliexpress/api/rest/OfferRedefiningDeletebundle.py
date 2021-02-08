from aliexpress.api.base import RestApi


class AliexpressOfferRedefiningDeletebundleRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.bundle_id = None

    def getapiname(self):
        return "aliexpress.offer.redefining.deletebundle"
