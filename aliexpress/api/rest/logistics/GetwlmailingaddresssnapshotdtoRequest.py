from aliexpress.api.base import RestApi


class AliexpressLogisticsGetwlmailingaddresssnapshotdtoRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.trade_order_id = None

    def getapiname(self):
        return "aliexpress.logistics.getwlmailingaddresssnapshotdto"
