from aliexpress.api.base import RestApi


class PostproductRedefiningEditaeproductRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.aeop_a_e_product = None

    def getapiname(self):
        return 'postproduct.redefining.editaeproduct'
