from aliexpress.api.base import RestApi


class PostproductRedefiningFindaeproductmodulebyidRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.module_id = None

    def getapiname(self):
        return 'postproduct.redefining.findaeproductmodulebyid'
