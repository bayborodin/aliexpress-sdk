from aliexpress.api.base import RestApi


class AliexpressPostproductRedefiningGetwindowproductsRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)

    def getapiname(self):
        return "aliexpress.postproduct.redefining.getwindowproducts"
