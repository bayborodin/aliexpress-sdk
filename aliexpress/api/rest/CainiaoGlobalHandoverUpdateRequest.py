from aliexpress.api.base import RestApi


class CainiaoGlobalHandoverUpdateRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.client = None
        self.handover_order_id = None
        self.locale = None
        self.order_code_list = None
        self.pickup_info = None
        self.remark = None
        self.return_info = None
        self.type = None
        self.user_info = None
        self.weight = None
        self.weight_unit = None

    def getapiname(self):
        return "cainiao.global.handover.update"
