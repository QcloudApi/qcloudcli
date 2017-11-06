# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateTicketStatusRequest(Request):

    def __init__(self):
        super(UpdateTicketStatusRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'UpdateTicketStatus', 'ticket.api.qcloud.com')

    def get_ownerUin(self):
        return self.get_params().get('ownerUin')

    def set_ownerUin(self, ownerUin):
        self.add_param('ownerUin', ownerUin)

    def get_statusId(self):
        return self.get_params().get('statusId')

    def set_statusId(self, statusId):
        self.add_param('statusId', statusId)

    def get_ticketIdList(self):
        return self.get_params().get('ticketIdList')

    def set_ticketIdList(self, ticketIdList):
        self.add_param('ticketIdList', ticketIdList)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
