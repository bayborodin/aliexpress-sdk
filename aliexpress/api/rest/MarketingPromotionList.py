from aliexpress.api.base import RestApi


class AliexpressMarketingPromotionListRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.marketing_promotion_query = None

    def getapiname(self):
        return "aliexpress.marketing.promotion.list"
