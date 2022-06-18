from aliexpress.api.base import RestApi


class PostproductRedefiningSetshopwindowproductRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.product_id_list = None

    def getapiname(self):
        return 'postproduct.redefining.setshopwindowproduct'
