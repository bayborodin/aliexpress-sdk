from aliexpress.api.base import RestApi


class AliexpressPostproductRedefiningFindaeproductmodulebyidRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.module_id = None

    def getapiname(self):
        return "aliexpress.postproduct.redefining.findaeproductmodulebyid"
