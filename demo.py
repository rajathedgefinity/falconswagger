from jsonmodels import models, fields, errors, validators


class Cat(models.Base):

    name = fields.StringField(required=True)
    breed = fields.StringField()
    love_humans = fields.IntField(nullable=True)


class Dog(models.Base):

    name = fields.StringField(required=True)
    age = fields.IntField()


class Car(models.Base):

    registration_number = fields.StringField(required=True)
    engine_capacity = fields.FloatField()
    color = fields.StringField()


class Person(models.Base):

    name = fields.StringField(required=True)
    surname = fields.StringField(required=True)
    nickname = fields.StringField(nullable=True)
    car = fields.EmbeddedField(Car)
    pets = fields.ListField([Cat, Dog], nullable=True)
