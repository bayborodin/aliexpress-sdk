from aliexpress.api.base import RestApi


class PostproductRedefiningFindaeproductprohibitedwordsRequest(
    RestApi
):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.category_id = None
        self.detail = None
        self.keywords = None
        self.product_properties = None
        self.title = None

    def getapiname(self):
        return 'postproduct.redefining.findaeproductprohibitedwords'
