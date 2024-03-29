from aliexpress.api.base import RestApi


class PostproductRedefiningEditproductcidattidskuRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.category_id = None
        self.product_id = None
        self.product_properties = None
        self.product_skus = None

    def getapiname(self):
        return 'postproduct.redefining.editproductcidattidsku'
