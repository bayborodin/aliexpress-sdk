from aliexpress.api.base import RestApi


class AliexpressMarketingStorepromotionProductsQueryRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.promotion_product_query_dto = None

    def getapiname(self):
        return "aliexpress.marketing.storepromotion.products.query"
