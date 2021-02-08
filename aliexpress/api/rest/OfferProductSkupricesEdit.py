from aliexpress.api.base import RestApi


class AliexpressOfferProductSkupricesEditRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.product_id = None
        self.sku_id_price_map = None

    def getapiname(self):
        return "aliexpress.offer.product.skuprices.edit"
