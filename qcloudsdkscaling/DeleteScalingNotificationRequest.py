#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteScalingNotificationRequest(Request):

	def __init__(self):
		Request.__init__(self, 'scaling', 'qcloudcliV1', 'DeleteScalingNotification', 'scaling.api.qcloud.com')

	def get_scalingGroupId(self):
		return self.get_params().get('scalingGroupId')

	def set_scalingGroupId(self, scalingGroupId):
		self.add_param('scalingGroupId', scalingGroupId)

	def get_notificationIds(self):
		return self.get_params().get('notificationIds')

	def set_notificationIds(self, notificationIds):
		self.add_param('notificationIds', notificationIds)

