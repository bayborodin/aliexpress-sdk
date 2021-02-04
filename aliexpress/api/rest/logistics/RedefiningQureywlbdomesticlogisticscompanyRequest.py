from aliexpress.api.base import RestApi


class AliexpressLogisticsRedefiningQureywlbdomesticlogisticscompanyRequest(
    RestApi
):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)

    def getapiname(self):
        return (
            "aliexpress.logistics.redefining.qureywlbdomesticlogisticscompany"
        )
