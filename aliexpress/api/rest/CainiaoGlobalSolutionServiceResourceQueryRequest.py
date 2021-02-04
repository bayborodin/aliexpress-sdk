from aliexpress.api.base import RestApi


class CainiaoGlobalSolutionServiceResourceQueryRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.locale = None
        self.seller_param = None
        self.sender_param = None
        self.solution_service_res_param = None

    def getapiname(self):
        return "cainiao.global.solution.service.resource.query"
