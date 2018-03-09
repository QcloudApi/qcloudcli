# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class QueryRequest(Request):

    def __init__(self):
        super(QueryRequest, self).__init__(
            'athena', 'qcloudcliV1', 'Query', 'athena.api.qcloud.com')

    def get_AccessChannelCode(self):
        return self.get_params().get('AccessChannelCode')

    def set_AccessChannelCode(self, AccessChannelCode):
        self.add_param('AccessChannelCode', AccessChannelCode)

    def get_InstanceId(self):
        return self.get_params().get('InstanceId')

    def set_InstanceId(self, InstanceId):
        self.add_param('InstanceId', InstanceId)

    def get_Query(self):
        return self.get_params().get('Query')

    def set_Query(self, Query):
        self.add_param('Query', Query)

    def get_RelatedKnowledgeMaxNum(self):
        return self.get_params().get('RelatedKnowledgeMaxNum')

    def set_RelatedKnowledgeMaxNum(self, RelatedKnowledgeMaxNum):
        self.add_param('RelatedKnowledgeMaxNum', RelatedKnowledgeMaxNum)

    def get_SessionId(self):
        return self.get_params().get('SessionId')

    def set_SessionId(self, SessionId):
        self.add_param('SessionId', SessionId)
