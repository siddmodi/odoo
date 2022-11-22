# Wizard is use to create transient models ie. popup showing wizard form.

from odoo import models, fields, api

class MarkLost(models.TransientModel):        #The difference is model.models form a table in db and models.TransientModel also create a table but it'll flushed after some time      
    _name = 'mark.lost'

    # request_id = fields.Many2one('travel.management', string="Request")
    lost_reason = fields.Text(string = 'Lost Reason')

    def action_mark_lost(self):
        print('Button clicked')