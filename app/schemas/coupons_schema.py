from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.coupons_model import CouponModel
from datetime import datetime


class DateTime(fields.DateTime):
    __schema_format__ = "DateTime"
    __schema_example__ = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

    def parse(self, value):
        if value is None:
            return None

        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            raise ValueError("Unsupported format for DateTime") from e

    def format(self, value: datetime):
        try:
            value = self.parse(value)
            return value.isoformat(timespec="seconds")
        except ValueError as e:
            raise fields.MarshallingError(e) from e


class CouponsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Coupon Create', {
            'code': fields.String(required=True, min_length=1, max_length=50),
            'procentage': fields.Float(required=True, precision=2),
            'started_ad': DateTime(required=True),
            'ended_ad': DateTime(required=True)
        })

    def update(self):
        return self.namespace.model('Coupon Update', {
            'code': fields.String(required=False, min_length=1, max_length=50),
            'procentage': fields.Float(required=False, precision=2),
            'started_ad': DateTime(required=False),
            'ended_ad': DateTime(required=False)
        })


class CouponsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CouponModel
        ordered = True
