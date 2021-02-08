from aliexpress.api.base import RestApi


class AliexpressCategoryRedefiningGetchildrenpostcategorybyidRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param0 = None

    def getapiname(self):
        return "aliexpress.category.redefining.getchildrenpostcategorybyid"
