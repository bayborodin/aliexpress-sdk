from aliexpress.api.base import RestApi


class AliexpressMessageRedefiningVersiontwoAddmsgRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.create_param = None

    def getapiname(self):
        return 'aliexpress.message.redefining.versiontwo.addmsg'
