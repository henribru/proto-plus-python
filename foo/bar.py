from typing import Generic, overload, TypeVar, NoReturn, Literal, Union, Optional, Type
import enum

class ProtoType(enum.IntEnum):
    """The set of basic types in protocol buffers."""

    # These values come from google/protobuf/descriptor.proto
    DOUBLE = 1
    FLOAT = 2
    INT64 = 3
    UINT64 = 4
    INT32 = 5
    FIXED64 = 6
    FIXED32 = 7
    BOOL = 8
    STRING = 9
    MESSAGE = 11
    BYTES = 12
    UINT32 = 13
    ENUM = 14
    SFIXED32 = 15
    SFIXED64 = 16
    SINT32 = 17
    SINT64 = 18


class Message:
    ...
    
class Enum:
    ...

T = TypeVar("T", bound=Union[float, int, bool, str, bytes, "Message", "Enum"])

class Field(Generic[T]):
    @overload
    def __init__(
        self: "Field[bytes]",
        proto_type: Literal[ProtoType.BYTES],
        *,
        number: int,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        # Why doesn't bytes, float etc. match here?
        proto_type: Type[T],
        *,
        number: int,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    def __init__(
        self,
        proto_type: Union[ProtoType, Type["Message"],  Type["Enum"], str],
        *,
        number: int,
        message: Optional[Union[Type["Message"],str]] = None,
        enum: Optional[Union[Type[Enum], str]] = None,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False
    ): ...
    
    @overload
    def __get__(self, obj: None, objtype: type["Message"]) -> str: ...
    @overload
    def __get__(self, obj: "Message", objtype: type["Message"]) -> T: ...
    def __get__(self, obj: Optional["Message"], objtype: type["Message"]) -> Union[str, T]: ...

class Foo(Message):
    a = Field(int, number=3)
    b = Field(str, number=5)
    c = Field(bool, number=6)
    d = Field(bytes, number=6)

reveal_type(Foo().a)
reveal_type(Foo().b)
reveal_type(Foo().c)
reveal_type(Foo().d)
