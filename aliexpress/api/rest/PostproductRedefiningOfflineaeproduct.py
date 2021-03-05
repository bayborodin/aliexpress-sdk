from aliexpress.api.base import RestApi


class PostproductRedefiningOfflineaeproductRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.product_ids = None

    def getapiname(self):
        return 'postproduct.redefining.offlineaeproduct'
