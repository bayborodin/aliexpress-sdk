from aliexpress.api.base import RestApi


class AliexpressMarketingLimitdiscountpromotionproductDelRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param_aeop_limited_disc_product_id_d_t_o = None

    def getapiname(self):
        return "aliexpress.marketing.limitdiscountpromotionproduct.del"
