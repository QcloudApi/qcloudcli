#!/usr/bin/env python
from . import enum


class BaseModule(object):
    def __init__(self, engine):
        self.engine = engine

    def __getattr__(self, func_name):
        def func(**kwargs):
            return self.engine.call(self.MODULE_NAME, func_name, kwargs)
        return func


class BaseMonitorDimension(object):
    METRIC_NAME = None
    NAME_SPACE = None

    def __init__(self, kwargs):
        kwargs.pop("self", 0)
        self.kwargs = kwargs

    def to_list(self):
        l = []
        for k, v in self.kwargs.items():
            l.append({"name": k, "value": v})
        return l


class EnumExt(enum.Enum):
    @classmethod
    def values(cls):
        return [x.value for x in cls]

    @property
    def name(self):
        return self._name_


class AutoIntEnum(EnumExt):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class StrEnum(str, EnumExt):
    pass


class IntEnum(int, EnumExt):
    def __str__(self):
        return str(self.value)

