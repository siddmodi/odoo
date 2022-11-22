from odoo import api, models, fields

class Sales2(models.Model):

    _inherit = "res.partner"

    # For make a field to attach files 
    attachments = fields.Binary(string="Attachments")
    attachment_ids = fields.Many2many('ir.attachment',string='Attachments')

    # For Projects
    project_count = fields.Integer(compute='_compute_project_count', string='Project Count')

    def _compute_project_count(self):
        # retrieve all children partners and prefetch 'parent_id' on them
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        project_groups = self.env['project.project'].read_group(             
            domain=[('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        partners = self.browse()
        for group in project_groups:
            partner = self.browse(group['partner_id'][0])
            while partner:
                if partner in self:
                    partner.project_count += group['partner_id_count']
                    partners |= partner
                partner = partner.parent_id
        (self - partners).project_count = 0


    def action_view_projects(self):
        action = self.env['ir.actions.act_window']._for_xml_id('project.open_view_project_all_config')
        all_child = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        action["domain"] = [("partner_id", "in", all_child.ids)]
        return action

