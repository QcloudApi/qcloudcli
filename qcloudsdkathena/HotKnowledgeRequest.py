# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class HotKnowledgeRequest(Request):

    def __init__(self):
        super(HotKnowledgeRequest, self).__init__(
            'athena', 'qcloudcliV1', 'HotKnowledge', 'athena.api.qcloud.com')

    def get_Count(self):
        return self.get_params().get('Count')

    def set_Count(self, Count):
        self.add_param('Count', Count)

    def get_HotKnowledgeCode(self):
        return self.get_params().get('HotKnowledgeCode')

    def set_HotKnowledgeCode(self, HotKnowledgeCode):
        self.add_param('HotKnowledgeCode', HotKnowledgeCode)

    def get_InstanceId(self):
        return self.get_params().get('InstanceId')

    def set_InstanceId(self, InstanceId):
        self.add_param('InstanceId', InstanceId)
