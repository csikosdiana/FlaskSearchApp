from wtforms import Form, StringField, SelectField


class ContactSearchForm(Form):
    choices = [
        ('Job history', 'Job history'),
        ('Company', 'Company'),
        ('Email', 'Email'),
        ('City', 'City'),
        ('Name', 'Name'),
        ('Country', 'Country')
    ]
    select = SelectField('Search contact by:', choices=choices)
    search = StringField('')
