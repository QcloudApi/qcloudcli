# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateTopicRequest(Request):

    def __init__(self):
        super(CreateTopicRequest, self).__init__(
            'mqiot', 'qcloudcliV1', 'CreateTopic', 'mqiot.api.qcloud.com')

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)

    def get_maxMsgCount(self):
        return self.get_params().get('maxMsgCount')

    def set_maxMsgCount(self, maxMsgCount):
        self.add_param('maxMsgCount', maxMsgCount)

    def get_maxMsgLife(self):
        return self.get_params().get('maxMsgLife')

    def set_maxMsgLife(self, maxMsgLife):
        self.add_param('maxMsgLife', maxMsgLife)

    def get_maxMsgSize(self):
        return self.get_params().get('maxMsgSize')

    def set_maxMsgSize(self, maxMsgSize):
        self.add_param('maxMsgSize', maxMsgSize)

    def get_topicName(self):
        return self.get_params().get('topicName')

    def set_topicName(self, topicName):
        self.add_param('topicName', topicName)
