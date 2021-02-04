from aliexpress.api.base import RestApi


class AliexpressMarketingLimitdiscountpromotionproductEditRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param_limited_disc_product_input_dto = None

    def getapiname(self):
        return "aliexpress.marketing.limitdiscountpromotionproduct.edit"
