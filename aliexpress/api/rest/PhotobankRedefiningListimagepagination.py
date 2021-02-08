from aliexpress.api.base import RestApi


class AliexpressPhotobankRedefiningListimagepaginationRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.aeop_image_pagination_request = None

    def getapiname(self):
        return "aliexpress.photobank.redefining.listimagepagination"
