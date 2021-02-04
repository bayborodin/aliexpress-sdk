from aliexpress.api.base import RestApi


class KfcKeywordSearchRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.apply = None
        self.content = None
        self.nick = None

    def getapiname(self):
        return "taobao.kfc.keyword.search"
