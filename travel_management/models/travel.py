# Search view (filter,groupby) ,  Graph view,  clean and logical field names   
# Age and gender (compute and related fields) filter and group by task 
# inside form view status trapped in progress requested closed, button  and submit --->> in progress, request---->> in progress to requested ,,, button should be invisible ,..........button close -------->> close status
# kanben view and add fields, alligned with css.
# add pivot view,x axis and y axis.............tree view group by employess by default by clicking on travel management...........put a domain(condition) to the entire module like male only when we click on travel managemnent.
# travel request male gender , female gender, all gender sub menus in dropdown
# Inherit company id invisible in the sale order list view or create a custom sale module do inheritance

# onchange functions gets executed during onchange of fields 

from typing_extensions import Required
from odoo import api, models, fields
from datetime import date
from datetime import datetime
import pdb
from dateutil import relativedelta
from odoo.exceptions import ValidationError
# 'Models' create modules and also create table in database
# 'Fields' use to create fields


class TravelManagement(models.Model):                                           # 'TravelManagement' is a python name
    _name = "travel.management"  
    _rec_name = 'employee_name'                                               # Database table name is 'travel_management'
    _description = 'Travel Management Description' 
    
    # employee_name = fields.Char(string='Employee Name', required=True)          # 'employee_name' is the column name in database table & 'Employee Name' is visbile on GUI side
    
    # editing
    employee_name = fields.Many2one('travel.management3',string="Employee Name", tracking = True)

    manager_name = fields.Char(string='Manager Name', required=True)

    employee_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male',related='employee_name.employee_gender', search='_search_employee_gender', store=True)
    
    employee_image = fields.Image(string='Employee Image',max_width=100,max_height=100,related='employee_name.employee_image') 

    note = fields.Text(string='Description')
    
    # company

    job_role = fields.Selection([
        ('full stack developer', 'Full Stack Developer'),
        ('backend developer', 'Backend Developer'),
        ('frontend developer', 'Frontend Developer'),
        ('selling','Selling'),
        ('purchasing','Purchasing'),
        ('managing employees','Managing Employees')
        ], string='Job Role' ,required=True)

    # department = fields.Selection([
    #     ('hr', 'HR'),
    #     ('it', 'IT'),
    #     ('sales', 'Sales'),
    #     ('purchase','Purchase')
    # ], string='Department', compute='_set_department')

    department = fields.Selection([
        ('hr', 'HR'),
        ('it', 'IT'),
        ('sales', 'Sales'),
        ('purchase','Purchase')
    ], string='Department', Required = True)
   
    source_location = fields.Char(string='Source Location', required=True)
    destination = fields.Char(string='Destination', required=True)
    flight_name = fields.Char(string='Flight Name', required=True)
    flight_number = fields.Char(string='Flight No.', required=True)
    no_of_days = fields.Integer(string='Number of days', required=True)
    date_of_arrival = fields.Datetime(string='Arrival Date Time')
    date_of_return = fields.Date(string='Return Date')
    current_status = fields.Text(string='Status Till Now')
    responsible_id = fields.Many2one('res.partner',string="Customer")  #created may2one field taking values from res.partner models (i.e customers which is in sales model). It is just like a selection field the difference is the values we select is not static here like in selection field, the values coming here are dynamic.
    one2many_field_ids = fields.One2many('travel.management2','field3',string='One2many field')   #One2many field is itself is a seprate model not the same model, It is a seprate model with its own views like tree view or form view etc.. , This model has fields define in 'TravelManagement2' model which is connected through Many2one field, here its field3
    tags_ids = fields.Many2many('res.partner.category',string='Tags')   # The many2many field is not in the travel management database existing table, instead of adding a feild to existing model it'll create a new relational table in database having id's of both table or foreign keys of both model. The formed table name set by default to first_model_name_second_model_name_rel
                                                                                     # After 'comodel' param 3 params are new formed table name and col names bcz by default odoo give table and col name by itself.
    

    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string="Age",compute='_compute_age',tracking=True)        # Compute field doesn't create a column in the table, if you still wanna create then use param 'force'

    currency_id = fields.Many2one('res.currency',string='Currency')
    salary = fields.Monetary(string='Salary')
    fees = fields.Float(string='Total Fees')

    is_intern = fields.Boolean(string='Is Intern')
    prescription = fields.Html(string='Prescription')
    future_date = fields.Date(string="Future date")

    state = fields.Selection([                                    # This is for status bar
        ('draft','Draft'),
        ('progress','Progress'),
        ('requested','Requested'),
        ('closed','Closed')
        ], string='Status',default='draft')


    @api.depends('date_of_birth')                                                   # To see real time changes in compute field we use @api.depends
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    @api.onchange('future_date')
    def onchange_future_date(self):
        if self.future_date and self.future_date < date.today():
            raise ValidationError("Please select the future date")


    def search_employee_gender(self, operator, value):
        return [('employee_gender','=','value')]

    def action_progress(self):
        for rec in self:
            rec.state = 'progress'

    def action_requested(self):
        for rec in self:
            rec.state = 'requested'

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    # def action_mark_lost(self):
    #     pass


    # def _search_age(self, operator, value):
    #     date_of_birth = date.today - relativedelta.relativedelta(years=value)
    #     start_of_year = date_of_birth.replace(day=1, month=1)
    #     end_of_year = date_of_birth.replace(day=31, month=12)
    #     return [('date_of_birth', '>=', start_of_year), ('date_of_birth', '<=', end_of_year)]

    # @api.depends('job_role')
    # def _set_department(self):
    #     if self.job_role:
    #         if self.job_role == 'full stack developer' or self.job_role == 'backend developer' or self.job_role == 'frontend developer':
    #             self.department == 'it'
    #         elif self.job_role == 'selling':
    #             self.department == 'sales'
    #         elif self.job_role == 'purchasing':
    #             self.department == 'purchase'
    #         elif self.job_role == 'managing employees':
    #             self.department == 'hr'


# 2nd model or class (We can define this here or in seprate .py file in same models directory)
class TravelManagement2(models.Model):                       #'TravelManagement2' is a python name                             
    _name = "travel.management2"                             # Database table name is 'travel_management2'                                                     
    _description = 'Travel Management 2 Description'          
    
    task = fields.Char(string='Task', required = True)                  # 'field1' is the column name in database table & 'Field 1' is visbile on GUI side
    percentage_completed = fields.Integer(string='% Completed')
    field3 = fields.Many2one('travel.management',string='Field 3')         # We have to create a many2one field in order to connect this model as one2many 



# 3rd model or class
class TravelManagement3(models.Model):                                                  
    _name = "travel.management3"  
    _rec_name = 'employee_first_name'                                                                            
    _description = 'Travel Management 3 Description'          
    
    employee_first_name = fields.Char(string='Employee First Name', required = True)     
    employee_second_name = fields.Char(string='Employee Second Name', required = True) 
    employee_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    employee_image = fields.Image(string='Employee Image',max_width=100,max_height=100)
    
