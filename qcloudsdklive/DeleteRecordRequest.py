# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteRecordRequest(Request):

    def __init__(self):
        super(DeleteRecordRequest, self).__init__(
            'live', 'qcloudcliV1', 'DeleteRecord', 'live.api.qcloud.com')

    def get_channelId(self):
        return self.get_params().get('channelId')

    def set_channelId(self, channelId):
        self.add_param('channelId', channelId)

    def get_taskId(self):
        return self.get_params().get('taskId')

    def set_taskId(self, taskId):
        self.add_param('taskId', taskId)
