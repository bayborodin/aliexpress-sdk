from aliexpress.api.base import RestApi


class RedefiningQuerytrackingresultRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.logistics_no = None
        self.origin = None
        self.out_ref = None
        self.service_name = None
        self.to_area = None

    def getapiname(self):
        return 'aliexpress.logistics.redefining.querytrackingresult'
