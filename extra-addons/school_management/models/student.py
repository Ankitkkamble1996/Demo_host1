from odoo import models, fields

class Student(models.Model):
    _name = "school.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    roll_number = fields.Char(string="Roll Number")
    student_class = fields.Char(string="Class")
    email = fields.Char(string="Email")
    mobail_no = fields.Integer(string="Mobaile No")