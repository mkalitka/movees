import peewee


db_file = peewee.SqliteDatabase(None)


class BaseModel(peewee.Model):
    class Meta:
        database = db_file
