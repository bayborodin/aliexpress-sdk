from aliexpress.api.base import RestApi


class AliexpressMarketingRedefiningFindsellercouponactivityRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.activity_id = None

    def getapiname(self):
        return "aliexpress.marketing.redefining.findsellercouponactivity"
