
class FindActivityForm(FlaskForm):
    city = StringField(required=True)
    category = StringField(required=True)
    name = StringField(required=True)
