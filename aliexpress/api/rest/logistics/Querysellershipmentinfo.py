from aliexpress.api.base import RestApi


class QuerysellershipmentinfoRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.logistics_no = None
        self.service_name = None
        self.sub_trade_order_index = None
        self.trade_order_id = None

    def getapiname(self):
        return 'aliexpress.logistics.querysellershipmentinfo'
