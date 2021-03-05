from aliexpress.api.base import RestApi


class SolutionBatchProductInventoryUpdateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.mutiple_product_update_list = None

    def getapiname(self):
        return 'solution.batch.product.inventory.update'
