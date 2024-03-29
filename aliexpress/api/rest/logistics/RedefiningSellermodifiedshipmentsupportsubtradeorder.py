from aliexpress.api.base import RestApi


class RedefiningSellermodifiedshipmentsupportsubtradeorderRequest(
    RestApi
):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.old_logistics_no = None
        self.old_service_name = None
        self.sub_trade_order_list = None
        self.trade_order_id = None

    def getapiname(self):
        return (
            'aliexpress.logistics.redefining.'
            'sellermodifiedshipmentsupportsubtradeorder'
        )
