from aliexpress.api.base import RestApi


class RedefiningVersiontwoQuerymsgdetaillistRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.channel_id = None
        self.current_page = None
        self.extern_id = None
        self.page_size = None

    def getapiname(self):
        return 'aliexpress.message.redefining.versiontwo.querymsgdetaillist'
