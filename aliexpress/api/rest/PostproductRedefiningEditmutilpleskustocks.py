from aliexpress.api.base import RestApi


class PostproductRedefiningEditmutilpleskustocksRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.product_id = None
        self.sku_stocks = None

    def getapiname(self):
        return 'postproduct.redefining.editmutilpleskustocks'
