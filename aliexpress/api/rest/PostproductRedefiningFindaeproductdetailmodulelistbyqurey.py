from aliexpress.api.base import RestApi


class PostproductRedefiningFindaeproductdetailmodulelistbyqureyRequest(
    RestApi
):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.module_status = None
        self.page_index = None
        self.type = None

    def getapiname(self):
        return 'postproduct.redefining.findaeproductdetailmodulelistbyqurey'
