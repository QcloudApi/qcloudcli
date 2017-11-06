# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListProductsRequest(Request):

    def __init__(self):
        super(ListProductsRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'ListProducts', 'iiot.api.qcloud.com')

    def get_maxResults(self):
        return self.get_params().get('maxResults')

    def set_maxResults(self, maxResults):
        self.add_param('maxResults', maxResults)

    def get_nextToken(self):
        return self.get_params().get('nextToken')

    def set_nextToken(self, nextToken):
        self.add_param('nextToken', nextToken)
