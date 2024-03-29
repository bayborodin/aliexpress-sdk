from aliexpress.api.base import RestApi


class CreateWarehouseOrderRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.address_d_t_os = None
        self.declare_product_d_t_os = None
        self.domestic_logistics_company = None
        self.domestic_logistics_company_id = None
        self.domestic_tracking_no = None
        self.insurance_coverage = None
        self.invoice_number = None
        self.package_num = None
        self.top_user_key = None
        self.trade_order_from = None
        self.trade_order_id = None
        self.undeliverable_decision = None
        self.warehouse_carrier_service = None

    def getapiname(self):
        return 'aliexpress.logistics.createwarehouseorder'
