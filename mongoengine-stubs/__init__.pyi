# re-export the submodules the same way as the original mongoengine package does

# Import submodules so that we can expose their __all__
from mongoengine import (
    connection,
    document,
    errors,
    fields,
    queryset,
    signals,
)

# Import everything from each submodule so that it can be accessed via
# mongoengine, e.g. instead of `from mongoengine.connection import connect`,
# users can simply use `from mongoengine import connect`, or even
# `from mongoengine import *` and then `connect('testdb')`.
from mongoengine.connection import *  # noqa: F401
from mongoengine.document import *  # noqa: F401
from mongoengine.errors import *  # noqa: F401
from mongoengine.fields import *  # noqa: F401
from mongoengine.queryset import *  # noqa: F401
from mongoengine.signals import *  # noqa: F401

__all__ = (
    list(document.__all__)
    + list(fields.__all__)
    + list(connection.__all__)
    + list(queryset.__all__)
    + list(signals.__all__)
    + list(errors.__all__)
)