from aliexpress.api.base import RestApi


class PostproductRedefiningSetgroupsRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.group_ids = None
        self.product_id = None

    def getapiname(self):
        return 'postproduct.redefining.setgroups'
