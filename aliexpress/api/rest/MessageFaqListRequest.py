from aliexpress.api.base import RestApi


class AliexpressMessageFaqListRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param_message_faq_query = None

    def getapiname(self):
        return "aliexpress.message.faq.list"
