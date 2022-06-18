from aliexpress.api.base import RestApi


class LogisticsRedefiningGetlogisticsselleraddressesRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.seller_address_query = None

    def getapiname(self):
        return 'logistics.redefining.getlogisticsselleraddresses'
