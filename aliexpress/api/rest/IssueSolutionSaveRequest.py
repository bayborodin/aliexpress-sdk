from aliexpress.api.base import RestApi


class AliexpressIssueSolutionSaveRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param_dto = None

    def getapiname(self):
        return "aliexpress.issue.solution.save"
