# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class QueryRequest(Request):

    def __init__(self):
        super(QueryRequest, self).__init__(
            'tbaas', 'qcloudcliV1', 'Query', 'tbaas.api.qcloud.com')

    def get_Args(self):
        return self.get_params().get('Args')

    def set_Args(self, Args):
        self.add_param('Args', Args)

    def get_Chaincode(self):
        return self.get_params().get('Chaincode')

    def set_Chaincode(self, Chaincode):
        self.add_param('Chaincode', Chaincode)

    def get_Channel(self):
        return self.get_params().get('Channel')

    def set_Channel(self, Channel):
        self.add_param('Channel', Channel)

    def get_ClusterId(self):
        return self.get_params().get('ClusterId')

    def set_ClusterId(self, ClusterId):
        self.add_param('ClusterId', ClusterId)

    def get_Func(self):
        return self.get_params().get('Func')

    def set_Func(self, Func):
        self.add_param('Func', Func)

    def get_Peers(self):
        return self.get_params().get('Peers')

    def set_Peers(self, Peers):
        self.add_param('Peers', Peers)
