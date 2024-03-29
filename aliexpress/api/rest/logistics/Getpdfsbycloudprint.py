from aliexpress.api.base import RestApi


class GetPdfsByCloudPrintRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.print_detail = None
        self.warehouse_order_query_d_t_os = None

    def getapiname(self):
        return 'aliexpress.logistics.getpdfsbycloudprint'
