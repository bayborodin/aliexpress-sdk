from aliexpress.api.base import RestApi


class AliexpressMarketingLimitdiscountpromotionCreateRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param_limited_disc_input_dto = None

    def getapiname(self):
        return "aliexpress.marketing.limitdiscountpromotion.create"
