# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateTopicRuleRequest(Request):

    def __init__(self):
        super(CreateTopicRuleRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'CreateTopicRule', 'iothub.api.qcloud.com')

    def get_ruleName(self):
        return self.get_params().get('ruleName')

    def set_ruleName(self, ruleName):
        self.add_param('ruleName', ruleName)

    def get_topicRulePayload(self):
        return self.get_params().get('topicRulePayload')

    def set_topicRulePayload(self, topicRulePayload):
        self.add_param('topicRulePayload', topicRulePayload)
