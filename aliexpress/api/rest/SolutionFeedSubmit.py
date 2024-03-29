from aliexpress.api.base import RestApi


class SolutionFeedSubmitRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.item_list = None
        self.operation_type = None

    def getapiname(self):
        return 'solution.feed.submit'
