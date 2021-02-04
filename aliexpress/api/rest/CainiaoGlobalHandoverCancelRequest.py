from aliexpress.api.base import RestApi


class CainiaoGlobalHandoverCancelRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.client = None
        self.handover_content_id = None
        self.handover_order_id = None
        self.locale = None
        self.tracking_number = None
        self.user_info = None

    def getapiname(self):
        return "cainiao.global.handover.cancel"
