from aliexpress.api.base import RestApi


class TradeSellerOrderlistGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param_aeop_order_query = None

    def getapiname(self):
        return 'aliexpress.trade.seller.orderlist.get'
