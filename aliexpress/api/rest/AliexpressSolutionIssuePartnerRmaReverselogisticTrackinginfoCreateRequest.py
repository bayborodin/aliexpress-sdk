"""
Created by auto_sdk on 2019.01.03
"""
from aliexpress.api.base import RestApi


class AliexpressSolutionIssuePartnerRmaReverselogisticTrackinginfoCreateRequest(
    RestApi
):
    def __init__(self, domain="gw.api.taobao.com", port=80):
        RestApi.__init__(self, domain, port)
        self.logistics_order_creation_request = None

    def getapiname(self):
        return (
            "aliexpress.solution.issue.partner.rma.reverselogistic.trackinginfo.create"
        )
