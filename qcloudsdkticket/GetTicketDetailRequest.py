# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetTicketDetailRequest(Request):

    def __init__(self):
        super(GetTicketDetailRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'GetTicketDetail', 'ticket.api.qcloud.com')

    def get_language(self):
        return self.get_params().get('language')

    def set_language(self, language):
        self.add_param('language', language)

    def get_ownerUin(self):
        return self.get_params().get('ownerUin')

    def set_ownerUin(self, ownerUin):
        self.add_param('ownerUin', ownerUin)

    def get_ticketId(self):
        return self.get_params().get('ticketId')

    def set_ticketId(self, ticketId):
        self.add_param('ticketId', ticketId)
