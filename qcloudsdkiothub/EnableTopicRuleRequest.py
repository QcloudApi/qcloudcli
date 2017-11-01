# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EnableTopicRuleRequest(Request):

    def __init__(self):
        super(EnableTopicRuleRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'EnableTopicRule', 'iothub.api.qcloud.com')

    def get_ruleName(self):
        return self.get_params().get('ruleName')

    def set_ruleName(self, ruleName):
        self.add_param('ruleName', ruleName)
