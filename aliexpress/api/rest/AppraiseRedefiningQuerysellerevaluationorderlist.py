from aliexpress.api.base import RestApi


class AliexpressAppraiseRedefiningQuerysellerevaluationorderlistRequest(
    RestApi
):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.query_d_t_o = None

    def getapiname(self):
        return 'aliexpress.appraise.redefining.querysellerevaluationorderlist'
