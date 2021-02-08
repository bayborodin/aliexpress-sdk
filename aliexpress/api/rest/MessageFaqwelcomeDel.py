from aliexpress.api.base import RestApi


class AliexpressMessageFaqwelcomeDelRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.param_message_faq_welcome_dto = None

    def getapiname(self):
        return "aliexpress.message.faqwelcome.del"
