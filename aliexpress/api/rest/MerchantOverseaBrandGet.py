from aliexpress.api.base import RestApi


class AliexpressMerchantOverseaBrandGetRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)

    def getapiname(self):
        return "aliexpress.merchant.oversea.brand.get"
