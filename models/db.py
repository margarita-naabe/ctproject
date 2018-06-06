from gluon.contrib.appconfig import AppConfig
configuration  = AppConfig(reload=True)


db = DAL("sqlite://storage.sqlite")
db.define_table("users",
                 Field('db_studentname'),
                 Field('db_id'),
                 Field('db_email'),
                 Field('db_password'))
