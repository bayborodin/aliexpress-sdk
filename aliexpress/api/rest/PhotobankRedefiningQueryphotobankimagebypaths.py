from aliexpress.api.base import RestApi


class AliexpressPhotobankRedefiningQueryphotobankimagebypathsRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.paths = None

    def getapiname(self):
        return "aliexpress.photobank.redefining.queryphotobankimagebypaths"
