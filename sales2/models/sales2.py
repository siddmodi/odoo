# #Create custom module 
# # Inherit sales tree view 
# # Hide company 
# # So if you install your module in odoo then in the sales module tree view company column should be hided 
# uninstall sales 2 automatically company_id will show, hide company_id  in form view

# sudo openvpn --config siddharth.modi__ssl_vpn_config.ovpn
# cloning..make changes... push.... pull....commit.....same line change and see the conflict and how to solve .......push and see changes in github server........make versions

# # class TravelManagement(models.Model):                                           # 'TravelManagement' is a python name
# #     _name = "travel.management"  
# #     _rec_name = 'employee_name'                                               # Database table name is 'travel_management'
# #     _description = 'Travel Management Description' 
    
# #     # employee_name = fields.Char(string='Employee Name', required=True)          # 'employee_name' is the column name in database table & 'Employee Name' is visbile on GUI side
    
# #     # editing
# #     employee_name = fields.Many2one('travel.management3',string="Employee Name", tracking = True)

# #     manager_name = fields.Char(string='Manager Name', required=True)

# #     employee_gender = fields.Selection([
# #         ('male', 'Male'),
# #         ('female', 'Female'),
# #         ('other', 'Other'),
# #     ], required=True, default='male',related='employee_name.employee_gender', search='_search_employee_gender', store=True)
    
# #     employee_image = fields.Image(string='Employee Image',max_width=100,max_height=100,related='employee_name.employee_image')

from odoo import api, models, fields

class Sales2(models.Model):
    _inherit = "res.partner"
    # project_count = fields.Integer(compute='_compute_project_count', string="Project Count")
    # sale_order_count = fields.Integer(compute='_compute_sale_order_count', string='Sale Order Count')

#     # _name = 'sales2'
#     # _rec_name = ""
#     _description = 'Sales2 Description' 

#     sid = fields.Char(string='sid')


# self is a recordset where we executing the function or code execution happens by (current model with id -- stating we are at this model at this record itself)
# Recordset is an object by which we can access its inner field and inner values, by using self. we can traverse inside the recordset
# Recordset is modelname(id)
# self.env is the odoo enviornment on which the action is triggered, we can use self.env.many_things_here like following.....
# 1.self.env.user give us the recordset of the current logged in user example- res.user(2,) where res.user is the model name and 2 is the id.
# As the above is the recordset we can traverse inside using dot opearator ex: self.env.user.name 
# 2. self.env.is_system returns whether the current user has group settings and superuser mode
# 3. self.env.is_superuser returns whether the current user is in superuser mode.
# 4. self.env.is_admin returns whether the current user has group "Access Rights" or it is in superuser mode.
# 5. self.env.is_system
# 6. self.env.company return the current company model with id. self.env.company.name return the name of the company. 
# 7. self.env.companies returns a recordset of the enabled companies by the user, ex: res.comapany(1,3).
# 8. self.env.lang will return the code of current langauage. ex: en_US.
# 9. self.env.cr return the db cursor object by which we perform the query operations inside the db. self.env.cr.execute(---) will perform the db operations.
# 10. self.env.context return context dictionary. self.env.context.get("--") to get any value of keys.
# 11. self.env.ref(external_id) use to get a recordset by its external id
# To get an enviornment of a separate object or model, self.env['hospital.appointment'] --model name inside[] and to get
# any recordset from that model use self.env['hospital.appointment'].browse(id) (ORM Method Browse return the recordset by taking id)


    # def open_view_project(self):
    #     action = self.env['ir.actions.act_window']._for_xml_id('project.open_view_project_all_config')
    #     if self.is_company:
    #         action['domain'] = [('partner_id.commercial_partner_id.id', '=', self.id)]
    #     else:
    #         action['domain'] = [('partner_id.id', '=', self.id)]
    #     return action

    # def _compute_project_count(self):
    #     project_data = self.env['project.project'].read_group([('project_id', 'in', self.ids), '|', '&', ('stage_id.is_closed', '=', False), ('stage_id.fold', '=', False), ('stage_id', '=', False)], ['project_id'], ['project_id'])
    #     result = dict((data['project_id'][0], data['project_id_count']) for data in project_data)
    #     for project in self:
    #         project.project_count = result.get(project.id, 0)


    # # For Sales
    # sale_order_count = fields.Integer(compute='_compute_sale_order_count', string='Sale Order Count')

    # def _compute_sale_order_count(self):
    # # retrieve all children partners and prefetch 'parent_id' on them
    #     all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
    #     all_partners.read(['parent_id'])

    #     sale_order_groups = self.env['sale.order'].read_group(
    #         domain=[('partner_id', 'in', all_partners.ids)],
    #         fields=['partner_id'], groupby=['partner_id']
    #     )
    #     partners = self.browse()
    #     for group in sale_order_groups:
    #         partner = self.browse(group['partner_id'][0])
    #         while partner:
    #             if partner in self:
    #                 partner.sale_order_count += group['partner_id_count']
    #                 partners |= partner
    #             partner = partner.parent_id
    #     (self - partners).sale_order_count = 0


    # def action_view_sale_order(self):
    #     action = self.env['ir.actions.act_window']._for_xml_id('sale.act_res_partner_2_sale_order')
    #     all_child = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
    #     action["domain"] = [("partner_id", "in", all_child.ids)]
    #     return action


    attachments = fields.Binary(string="Attachments")
    # attachment_name = fields.Char(string="File Name")
    attachment_ids = fields.Many2many('ir.attachment',string='Attachments')

    # For Projectss
    project_count = fields.Integer(compute='_compute_project_count', string='Project Count')

    def _compute_project_count(self):
        # retrieve all children partners and prefetch 'parent_id' on them
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        sale_order_groups = self.env['project.project'].read_group(             
            domain=[('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        partners = self.browse()
        for group in sale_order_groups:
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

 # se_customer_master 
