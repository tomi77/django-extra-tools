def convert_values(self, value, field):
    """Coerce the value returned by the database backend into a consistent type that
    is compatible with the field type.
    """
    internal_type = field.get_internal_type()
    if internal_type == 'DecimalField':
        return value
    elif internal_type and internal_type.endswith('IntegerField') or internal_type == 'AutoField':
        return int(value)
    elif internal_type in ('DateField', 'DateTimeField', 'TimeField', 'CharField', 'EmailField', 'SlugField',
                           'URLField'):
        return value
    # No field, or the field isn't known to be a decimal or integer
    # Default to a float
    return float(value)
