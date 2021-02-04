from aliexpress.api.base import RestApi


class AliexpressIssueIssuelistGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.query_dto = None

    def getapiname(self):
        return "aliexpress.issue.issuelist.get"
