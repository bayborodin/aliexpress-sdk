from aliexpress.api.base import RestApi


class AliexpressPhotobankRedefiningDelunusephotoRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.aeop_delete_image_request = None

    def getapiname(self):
        return 'aliexpress.photobank.redefining.delunusephoto'
