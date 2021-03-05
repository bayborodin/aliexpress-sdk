from aliexpress.api.base import RestApi


class PostproductRedefiningGetsizechartinfobycategoryidRequest(
    RestApi
):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.category_id = None

    def getapiname(self):
        return 'postproduct.redefining.getsizechartinfobycategoryid'
