from aliexpress.api.base import RestApi


class AliexpressLogisticsValueaddedInsuranceEstimateRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.insurance_coverage = None
        self.solution_code = None
        self.trade_order_id = None

    def getapiname(self):
        return "aliexpress.logistics.valueadded.insurance.estimate"
