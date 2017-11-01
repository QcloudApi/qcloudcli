# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RemindTicketRequest(Request):

    def __init__(self):
        super(RemindTicketRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'RemindTicket', 'ticket.api.qcloud.com')
