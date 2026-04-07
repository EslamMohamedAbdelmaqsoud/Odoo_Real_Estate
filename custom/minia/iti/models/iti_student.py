from odoo import models, fields


class ITIStudent(models.Model):
    _name = 'iti.student'  # name of module
    _description = 'ITI Student'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date', required=True)
    salary = fields.Float(string='Salary', required=True)
    address = fields.Text(string='Address')
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('other', 'Other')
    ])
    accepted = fields.Boolean(string='Accepted')
    level = fields.Integer(string='Level')
    image = fields.Binary(string='Image')
    cv = fields.Html()
    login_time = fields.Datetime(string='Login Time')
