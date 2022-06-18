from aliexpress.api.base import RestApi


class SolutionFeedQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.job_id = None

    def getapiname(self):
        return 'solution.feed.query'
