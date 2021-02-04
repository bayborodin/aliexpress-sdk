from aliexpress.api.base import RestApi


class AliexpressOfferRedefiningGetsizetemplatesbycategoryidRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.current_page = None
        self.leaf_category_id = None

    def getapiname(self):
        return "aliexpress.offer.redefining.getsizetemplatesbycategoryid"
