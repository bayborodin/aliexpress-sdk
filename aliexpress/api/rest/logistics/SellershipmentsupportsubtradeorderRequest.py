from aliexpress.api.base import RestApi


class AliexpressLogisticsSellershipmentsupportsubtradeorderRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.sub_trade_order_list = None
        self.trade_order_id = None

    def getapiname(self):
        return "aliexpress.logistics.sellershipmentsupportsubtradeorder"
