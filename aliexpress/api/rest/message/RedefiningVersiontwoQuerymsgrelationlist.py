from aliexpress.api.base import RestApi


class RedefiningVersiontwoQuerymsgrelationlistRequest(
    RestApi
):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.query = None

    def getapiname(self):
        return 'aliexpress.message.redefining.versiontwo.querymsgrelationlist'
