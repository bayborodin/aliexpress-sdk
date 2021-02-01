"""
Created by auto_sdk on 2020.05.27
"""
from aliexpress.api.base import RestApi


class AliexpressLogisticsSellershipmentfortopRequest(RestApi):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.description = None
        self.logistics_no = None
        self.out_ref = None
        self.package_type = None
        self.send_type = None
        self.service_name = None
        self.tracking_website = None

    def getapiname(self):
        return "aliexpress.logistics.sellershipmentfortop"
