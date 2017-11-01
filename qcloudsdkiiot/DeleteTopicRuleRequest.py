# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteTopicRuleRequest(Request):

    def __init__(self):
        super(DeleteTopicRuleRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'DeleteTopicRule', 'iiot.api.qcloud.com')

    def get_ruleName(self):
        return self.get_params().get('ruleName')

    def set_ruleName(self, ruleName):
        self.add_param('ruleName', ruleName)
