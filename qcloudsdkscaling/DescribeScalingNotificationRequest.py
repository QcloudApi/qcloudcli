# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScalingNotificationRequest(Request):

    def __init__(self):
        super(DescribeScalingNotificationRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeScalingNotification', 'scaling.api.qcloud.com')

    def get_notificationIds(self):
        return self.get_params().get('notificationIds')

    def set_notificationIds(self, notificationIds):
        self.add_param('notificationIds', notificationIds)

    def get_notificationName(self):
        return self.get_params().get('notificationName')

    def set_notificationName(self, notificationName):
        self.add_param('notificationName', notificationName)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)
