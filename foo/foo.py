import proto
from proto.primitives import ProtoType
from typing import reveal_type
from proto.fields import Message

class Bar(proto.Message):
    pass

class Baz(proto.Enum):
    BAZ = 0

class Foo(Message):
    double = proto.Field(proto.DOUBLE, number=36)
    int = proto.Field(proto.INT32, number=1)
    bool = proto.Field(proto.BOOL, number=2)
    string = proto.Field(proto.STRING, number=3)
    bytes = proto.Field(proto.BYTES, number=4)
    bar_message_1 = proto.Field(proto.MESSAGE, number=5, message=Bar)
    bar_message_2 = proto.Field(Bar, number=6)
    baz_enum_1 = proto.Field(proto.ENUM, number=7, enum=Baz)
    baz_enum_2 = proto.Field(Baz, number=8)
    foo1 = proto.Field(bool, number=9)
    foo2 = proto.Field(str, number=9)
    foo3 = proto.Field(bytes, number=9)
    foo3 = proto.Field(int, number=9)
    bar = proto.Field(proto.MESSAGE, number=9, message=bool)

    double_repeated = proto.RepeatedField(proto.DOUBLE, number=9)
    int_repeated = proto.RepeatedField(proto.INT32, number=10)
    bool_repeated = proto.RepeatedField(proto.BOOL, number=11)
    string_repeated = proto.RepeatedField(proto.STRING, number=12)
    bytes_repeated = proto.RepeatedField(proto.BYTES, number=13)
    bar_message_repeated_1 = proto.RepeatedField(proto.MESSAGE, number=14, message=Bar.pb())
    bar_message_repeated_2 = proto.RepeatedField(Bar, number=15)
    baz_enum_repeated_1 = proto.RepeatedField(proto.ENUM, number=16, enum=Baz)
    baz_enum_repeated_2 = proto.RepeatedField(Baz, number=17)

    string_double_map = proto.MapField(ProtoType.STRING, ProtoType.DOUBLE, number=18)
    string_int_map = proto.MapField(ProtoType.STRING, ProtoType.INT32, number=19)
    string_bool_map = proto.MapField(ProtoType.STRING, ProtoType.BOOL, number=20)
    string_string_map = proto.MapField(ProtoType.STRING, ProtoType.STRING, number=21)
    string_bytes_map = proto.MapField(ProtoType.STRING, ProtoType.BYTES, number=22)
    string_bar_message_map_1 = proto.MapField(ProtoType.STRING, ProtoType.MESSAGE, number=23, message=Bar)
    string_bar_message_map_2 = proto.MapField(ProtoType.STRING, Bar, number=24)
    string_baz_enum_map_1 = proto.MapField(ProtoType.STRING, ProtoType.ENUM, number=25, enum=Baz)
    string_baz_enum_map_2 = proto.MapField(ProtoType.STRING, Baz, number=26)
    int_double_map = proto.MapField(ProtoType.INT32, ProtoType.DOUBLE, number=27)
    int_int_map = proto.MapField(ProtoType.INT32, ProtoType.INT32, number=28)
    int_bool_map = proto.MapField(ProtoType.INT32, ProtoType.BOOL, number=29)
    int_string_map = proto.MapField(ProtoType.INT32, ProtoType.STRING, number=30)
    int_bytes_map = proto.MapField(ProtoType.INT32, ProtoType.BYTES, number=31)
    int_bar_message_map_1 = proto.MapField(ProtoType.INT32, ProtoType.MESSAGE, number=32, message=Bar)
    int_bar_message_map_2 = proto.MapField(ProtoType.INT32, Bar, number=33)
    int_baz_enum_map_1 = proto.MapField(ProtoType.INT32, ProtoType.ENUM, number=34, enum=Baz)
    int_baz_enum_map_2 = proto.MapField(ProtoType.INT32, Baz, number=35)

foo = Foo()

reveal_type(foo.foo)
print(isinstance(foo.foo, Bar))

reveal_type(foo.double)  # float
reveal_type(foo.int)  # int
reveal_type(foo.bool)  # bool
reveal_type(foo.string)  # str
reveal_type(foo.bytes)  # bytes
reveal_type(foo.bar_message_1)  # Bar
reveal_type(foo.bar_message_2)  # Bar
reveal_type(foo.baz_enum_1)  # Baz
reveal_type(foo.baz_enum_2)  # Baz
reveal_type(foo.double_repeated)  # list[float]
reveal_type(foo.int_repeated)  # list[int] 
reveal_type(foo.bool_repeated)  # list[bool]
reveal_type(foo.string_repeated)  # list[str]
reveal_type(foo.bytes_repeated)  # list[bytes]
reveal_type(foo.bar_message_repeated_1)  # list[Bar]
reveal_type(foo.bar_message_repeated_2)  # list[Bar]
reveal_type(foo.baz_enum_repeated_1)  # list[Baz]
reveal_type(foo.baz_enum_repeated_2)  # list[Baz]
reveal_type(foo.string_double_map)  # dict[str, float]
reveal_type(foo.string_int_map)  # dict[str, int]
reveal_type(foo.string_bool_map)  # dict[string, bool]
reveal_type(foo.string_string_map)  # dict[str, str]
reveal_type(foo.string_bytes_map)  # dict[str, bytes]
reveal_type(foo.string_bar_message_map_1)  # dict[str, Bar]
reveal_type(foo.string_bar_message_map_2)  # dict[str, Bar]
reveal_type(foo.string_baz_enum_map_1)  # dict[str, Baz]
reveal_type(foo.string_baz_enum_map_2)  # dict[str, Baz]
reveal_type(foo.int_double_map)  # dict[int, float]
reveal_type(foo.int_int_map)  # dict[int, int]
reveal_type(foo.int_bool_map)  # dict[int, bool]
reveal_type(foo.int_string_map)  # dict[int, str]
reveal_type(foo.int_bytes_map)  # dict[int, bytes]
reveal_type(foo.int_bar_message_map_1)  # dict[int, Bar]
reveal_type(foo.int_bar_message_map_2)  # dict[int, Bar]
reveal_type(foo.int_baz_enum_map_1)  # dict[int, Baz]
reveal_type(foo.int_baz_enum_map_2)  # dict[int, Baz]

reveal_type(Foo.pb)
reveal_type(Foo.wrap)
reveal_type(Foo.serialize)
reveal_type(Foo.deserialize)
reveal_type(Foo.to_json)
reveal_type(Foo.from_json)
reveal_type(Foo.to_dict)
reveal_type(Foo.copy_from)
reveal_type(Foo)

reveal_type(Foo.pb())
reveal_type(Foo.pb(None))
reveal_type(Foo.pb(foo))
reveal_type(Foo.wrap(Foo.pb(foo)))
reveal_type(Foo.serialize(foo))
reveal_type(Foo.deserialize(Foo.serialize(foo)))
reveal_type(Foo.to_json(foo))
reveal_type(Foo.from_json(Foo.to_json(foo)))
reveal_type(Foo.to_dict(foo))
reveal_type(Foo.copy_from(foo, foo))
reveal_type(Foo(foo))

reveal_type(Foo()._pb)

Foo.pb(Foo())
#Foo.pb(Foo.pb(Foo()))
#Foo.pb(Foo.to_dict(Foo()))
#Foo.pb(Foo.pb(Foo()), coerce=False)
#Foo.pb(Foo.to_dict(Foo()), coerce=False)
Foo.pb(Foo.pb(Foo()), coerce=True)
Foo.pb(Foo.to_dict(Foo()), coerce=True)

# reveal_type(Foo().foo)