# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteTopicRequest(Request):

    def __init__(self):
        super(DeleteTopicRequest, self).__init__(
            'mqiot', 'qcloudcliV1', 'DeleteTopic', 'mqiot.api.qcloud.com')

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)

    def get_topicName(self):
        return self.get_params().get('topicName')

    def set_topicName(self, topicName):
        self.add_param('topicName', topicName)
