from aliexpress.api.base import RestApi


class SolutionFeedListGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.current_page = None
        self.feed_type = None
        self.page_size = None
        self.status = None

    def getapiname(self):
        return 'solution.feed.list.get'
