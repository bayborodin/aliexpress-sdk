from aliexpress.api.base import RestApi


class AliexpressPostproductRedefiningPostmultilanguageaeproductRequest(
    RestApi
):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.product = None

    def getapiname(self):
        return "aliexpress.postproduct.redefining.postmultilanguageaeproduct"
