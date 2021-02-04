from aliexpress.api.base import RestApi


class FilesGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.end_date = None
        self.start_date = None
        self.status = None

    def getapiname(self):
        return "taobao.files.get"
