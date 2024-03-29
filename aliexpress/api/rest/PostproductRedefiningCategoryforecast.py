from aliexpress.api.base import RestApi


class PostproductRedefiningCategoryforecastRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.forecast_mode = None
        self.is_filter_by_permission = None
        self.locale = None
        self.subject = None

    def getapiname(self):
        return 'postproduct.redefining.categoryforecast'
