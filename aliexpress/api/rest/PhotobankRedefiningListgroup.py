from aliexpress.api.base import RestApi


class AliexpressPhotobankRedefiningListgroupRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.group_id = None

    def getapiname(self):
        return 'aliexpress.photobank.redefining.listgroup'
