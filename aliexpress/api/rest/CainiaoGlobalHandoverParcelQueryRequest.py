from aliexpress.api.base import RestApi


class CainiaoGlobalHandoverParcelQueryRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.client = None
        self.locale = None
        self.order_code = None
        self.tracking_number = None
        self.user_info = None

    def getapiname(self):
        return "cainiao.global.handover.parcel.query"
