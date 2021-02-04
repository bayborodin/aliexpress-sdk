from aliexpress.api.base import RestApi


class AliexpressMessageFaqwelcomeAddRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param_list = None

    def getapiname(self):
        return "aliexpress.message.faqwelcome.add"
