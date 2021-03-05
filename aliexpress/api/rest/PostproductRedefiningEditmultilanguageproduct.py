from aliexpress.api.base import RestApi


class PostproductRedefiningEditmultilanguageproductRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.aeop_a_e_product_multilanguage_info = None
        self.product_id = None

    def getapiname(self):
        return 'postproduct.redefining.editmultilanguageproduct'
