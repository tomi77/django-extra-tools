from django.core.exceptions import ObjectDoesNotExist
from tastypie import fields, resources


class CreatedAtMixin(resources.Resource):
    """Add ``created_at`` field to resource"""
    created_at = fields.DateTimeField('created_at', readonly=True, null=True)


class CreatedByMixin(resources.Resource):
    """Add ``created_by_name`` field to resource"""
    created_by_name = fields.CharField(readonly=True)

    @staticmethod
    def dehydrate_created_by_name(bundle):
        try:
            return '{} {}'.format(bundle.obj.created_by.first_name,
                                  bundle.obj.created_by.last_name).strip()
        except ObjectDoesNotExist:
            return None


class CreatedMixin(CreatedAtMixin, CreatedByMixin):
    pass


class UpdatedAtMixin(resources.Resource):
    updated_at = fields.DateTimeField('updated_at', readonly=True, null=True)


class UpdatedByMixin(resources.Resource):
    updated_by_name = fields.CharField(readonly=True)

    @staticmethod
    def dehydrate_updated_by_name(bundle):
        if bundle.obj.updated_by is None:
            return None
        return '{} {}'.format(bundle.obj.updated_by.first_name,
                              bundle.obj.updated_by.last_name).strip()


class UpdatedMixin(UpdatedAtMixin, UpdatedByMixin):
    pass
