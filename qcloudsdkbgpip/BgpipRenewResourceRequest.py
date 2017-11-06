# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class BgpipRenewResourceRequest(Request):

    def __init__(self):
        super(BgpipRenewResourceRequest, self).__init__(
            'bgpip', 'qcloudcliV1', 'BgpipRenewResource', 'bgpip.api.qcloud.com')

    def get_curDeadline(self):
        return self.get_params().get('curDeadline')

    def set_curDeadline(self, curDeadline):
        self.add_param('curDeadline', curDeadline)

    def get_extendTime(self):
        return self.get_params().get('extendTime')

    def set_extendTime(self, extendTime):
        self.add_param('extendTime', extendTime)

    def get_region(self):
        return self.get_params().get('region')

    def set_region(self, region):
        self.add_param('region', region)

    def get_resourceId(self):
        return self.get_params().get('resourceId')

    def set_resourceId(self, resourceId):
        self.add_param('resourceId', resourceId)

    def get_timeSpan(self):
        return self.get_params().get('timeSpan')

    def set_timeSpan(self, timeSpan):
        self.add_param('timeSpan', timeSpan)

    def get_timeUnit(self):
        return self.get_params().get('timeUnit')

    def set_timeUnit(self, timeUnit):
        self.add_param('timeUnit', timeUnit)
