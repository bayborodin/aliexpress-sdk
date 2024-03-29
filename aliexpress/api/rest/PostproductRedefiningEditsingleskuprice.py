from aliexpress.api.base import RestApi


class PostproductRedefiningEditsingleskupriceRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.product_id = None
        self.sku_id = None
        self.sku_price = None

    def getapiname(self):
        return 'postproduct.redefining.editsingleskuprice'
