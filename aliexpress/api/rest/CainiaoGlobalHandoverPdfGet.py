from aliexpress.api.base import RestApi


class CainiaoGlobalHandoverPdfGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.client = None
        self.handover_content_id = None
        self.locale = None
        self.type = None
        self.user_info = None

    def getapiname(self):
        return "cainiao.global.handover.pdf.get"
