# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyScheduledTaskRequest(Request):

    def __init__(self):
        super(ModifyScheduledTaskRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'ModifyScheduledTask', 'scaling.api.qcloud.com')

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_readjustDesiredCapacity(self):
        return self.get_params().get('readjustDesiredCapacity')

    def set_readjustDesiredCapacity(self, readjustDesiredCapacity):
        self.add_param('readjustDesiredCapacity', readjustDesiredCapacity)

    def get_readjustMaxSize(self):
        return self.get_params().get('readjustMaxSize')

    def set_readjustMaxSize(self, readjustMaxSize):
        self.add_param('readjustMaxSize', readjustMaxSize)

    def get_readjustMinSize(self):
        return self.get_params().get('readjustMinSize')

    def set_readjustMinSize(self, readjustMinSize):
        self.add_param('readjustMinSize', readjustMinSize)

    def get_recurrence(self):
        return self.get_params().get('recurrence')

    def set_recurrence(self, recurrence):
        self.add_param('recurrence', recurrence)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)

    def get_scalingScheduledTaskId(self):
        return self.get_params().get('scalingScheduledTaskId')

    def set_scalingScheduledTaskId(self, scalingScheduledTaskId):
        self.add_param('scalingScheduledTaskId', scalingScheduledTaskId)

    def get_scalingScheduledTaskName(self):
        return self.get_params().get('scalingScheduledTaskName')

    def set_scalingScheduledTaskName(self, scalingScheduledTaskName):
        self.add_param('scalingScheduledTaskName', scalingScheduledTaskName)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)
