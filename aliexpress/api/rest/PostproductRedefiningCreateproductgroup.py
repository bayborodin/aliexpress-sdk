from aliexpress.api.base import RestApi


class PostproductRedefiningCreateproductgroupRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.name = None
        self.parent_id = None

    def getapiname(self):
        return 'postproduct.redefining.createproductgroup'
