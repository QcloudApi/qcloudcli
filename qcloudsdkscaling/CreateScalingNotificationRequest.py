# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateScalingNotificationRequest(Request):

    def __init__(self):
        super(CreateScalingNotificationRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'CreateScalingNotification', 'scaling.api.qcloud.com')

    def get_notificationName(self):
        return self.get_params().get('notificationName')

    def set_notificationName(self, notificationName):
        self.add_param('notificationName', notificationName)

    def get_notificationTypes(self):
        return self.get_params().get('notificationTypes')

    def set_notificationTypes(self, notificationTypes):
        self.add_param('notificationTypes', notificationTypes)

    def get_receiversIds(self):
        return self.get_params().get('receiversIds')

    def set_receiversIds(self, receiversIds):
        self.add_param('receiversIds', receiversIds)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)
