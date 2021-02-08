from aliexpress.api.base import RestApi


class AliexpressCategoryRedefiningGetallchildattributesresultRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.cate_id = None
        self.locale = None
        self.parent_attrvalue_list = None

    def getapiname(self):
        return "aliexpress.category.redefining.getallchildattributesresult"
