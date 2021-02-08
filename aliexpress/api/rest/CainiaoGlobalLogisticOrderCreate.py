from aliexpress.api.base import RestApi


class CainiaoGlobalLogisticOrderCreateRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.locale = None
        self.order_param = None

    def getapiname(self):
        return "cainiao.global.logistic.order.create"
