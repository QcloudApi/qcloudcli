# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListTopicRulesRequest(Request):

    def __init__(self):
        super(ListTopicRulesRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'ListTopicRules', 'iiot.api.qcloud.com')

    def get_maxResults(self):
        return self.get_params().get('maxResults')

    def set_maxResults(self, maxResults):
        self.add_param('maxResults', maxResults)

    def get_nextToken(self):
        return self.get_params().get('nextToken')

    def set_nextToken(self, nextToken):
        self.add_param('nextToken', nextToken)

    def get_ruleDisabled(self):
        return self.get_params().get('ruleDisabled')

    def set_ruleDisabled(self, ruleDisabled):
        self.add_param('ruleDisabled', ruleDisabled)

    def get_topic(self):
        return self.get_params().get('topic')

    def set_topic(self, topic):
        self.add_param('topic', topic)
