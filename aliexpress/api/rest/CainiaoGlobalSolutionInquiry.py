from aliexpress.api.base import RestApi


class CainiaoGlobalSolutionInquiryRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.locale = None
        self.package_params = None
        self.seller_info_param = None
        self.trade_order_param = None

    def getapiname(self):
        return "cainiao.global.solution.inquiry"
