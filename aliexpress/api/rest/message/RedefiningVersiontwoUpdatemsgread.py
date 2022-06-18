from aliexpress.api.base import RestApi


class RedefiningVersiontwoUpdatemsgreadRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.channel_id = None

    def getapiname(self):
        return 'aliexpress.message.redefining.versiontwo.updatemsgread'
