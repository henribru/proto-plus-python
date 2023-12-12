# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import EnumMeta
from typing import overload, TypeVar, MutableMapping, MutableSequence, TYPE_CHECKING, Generic, Any, Optional, Union, Type, NoReturn


from typing_extensions import Literal
from google.protobuf import descriptor_pb2
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper
from google.protobuf import message

from proto.primitives import ProtoType

if TYPE_CHECKING:
    from proto.message import Message
    from proto.enums import Enum

IntegerProtoType = Literal[
    ProtoType.INT64,
    ProtoType.UINT64,
    ProtoType.INT32,
    ProtoType.FIXED64,
    ProtoType.FIXED32,
    ProtoType.UINT32,
    ProtoType.SFIXED32,
    ProtoType.SFIXED64,
    ProtoType.SINT32,
    ProtoType.SINT64,
]

class Message:
    ...
    
class Enum:
    ...

T = TypeVar("T", bound=Union[float, int, bool, str, bytes, "Message", "Enum"])

class Field(Generic[T]):
    """A representation of a type of field in protocol buffers."""

    # Fields are NOT repeated nor maps.
    # The RepeatedField overrides this values.
    repeated = False

    # Field(ProtoType.DOUBLE) -> float
    # @overload
    # def __init__(
    #     self: "Field[float]",
    #     proto_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
    #     *,
    #     number: int,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # # Field(ProtoType.INT64) -> int
    # @overload
    # def __init__(
    #     self: "Field[int]",
    #     proto_type: IntegerProtoType,
    #     *,
    #     number: int,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field(ProtoType.BOOL) -> bool
    # @overload
    # def __init__(
    #     self: "Field[bool]",
    #     proto_type: Literal[ProtoType.BOOL],
    #     *,
    #     number: int,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # # Field(ProtoType.STRING) -> string
    # @overload
    # def __init__(
    #     self: "Field[str]",
    #     proto_type: Literal[ProtoType.STRING],
    #     *,
    #     number: int,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # # Field(ProtoType.BYTES) -> bytes
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
    # # Field(ProtoType.MESSAGE, message=PlainProtobufMessage) -> Any
    # @overload
    # def __init__(
    #     self: "Field[Any]",
    #     proto_type: Literal[ProtoType.MESSAGE],
    #     *,
    #     number: int,
    #     message: Type[message.Message],
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field(ProtoType.MESSAGE, message=int) -> NoReturn
    # @overload
    # def __init__(
    #     self: Field[NoReturn],
    #     proto_type: Literal[ProtoType.MESSAGE],
    #     *,
    #     number: int,
    #     message: Type[Union[float, int, bool, str, bytes, "Enum"]],
    #     #message: Union[Type[float], Type[int], Type[bool], Type[str], Type[bytes], Type["Enum"]],
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field(ProtoType.MESSAGE, message=ProtoPlusMessage) -> ProtoPlusMessage
    # @overload
    # def __init__(
    #     self: "Field[T]",
    #     proto_type: Literal[ProtoType.MESSAGE],
    #     *,
    #     number: int,
    #     message: type[T],
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # # Field(ProtoType.ENUM, message=PlainProtobufEnum) -> Any
    # @overload
    # def __init__(
    #     self: "Field[Any]",
    #     proto_type: Literal[ProtoType.ENUM],
    #     *,
    #     number: int,
    #     enum: type[EnumTypeWrapper],
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field(ProtoType.ENUM, enum=int) -> NoReturn
    # @overload
    # def __init__(
    #     self: Field[NoReturn],
    #     proto_type: Literal[ProtoType.ENUM],
    #     *,
    #     number: int,
    #     # We can't include int or float here because those will match proto.Enum since it's an IntEnum.
    #     enum: Type[Union[bool, str, bytes, "Message"]],
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field(ProtoType.ENUM, enum=ProtoPlusEnum) -> ProtoPlusEnum
    # @overload
    # def __init__(
    #     self: "Field[T]",
    #     proto_type: Literal[ProtoType.ENUM],
    #     *,
    #     number: int,
    #     enum: type[T],
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # # Field(PlainProtobufMessage) -> Any
    # @overload
    # def __init__(
    #     self: "Field[Any]",
    #     proto_type: Type[message.Message],
    #     *,
    #     number: int,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # # Field(PlainProtobufEnum) -> Any
    # @overload
    # def __init__(
    #     self: "Field[Any]",
    #     proto_type: Type[EnumTypeWrapper],
    #     *,
    #     number: int,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field(int) -> NoReturn
    # @overload
    # def __init__(
    #     self: Field[Any],
    #     # We can't include int or float here because those will match proto.Enum since it's an IntEnum.
    #     proto_type: Type[Union[bool, str, bytes]],
    #     *,
    #     number: int,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field(ProtoPlusMessage) -> ProtoPlusMessage
    # Field(ProtoPlusEnum) -> ProtoPlusEnum
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
    # Field(ProtoType.MESSAGE, message="ProtoPlusMessage") -> Any
    # @overload
    # def __init__(
    #     self: "Field[Any]",
    #     proto_type: Literal[ProtoType.MESSAGE],
    #     *,
    #     number: int,
    #     message: str,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field(ProtoType.ENUM, enum="ProtoPlusEnum") -> Any
    # @overload
    # def __init__(
    #     self: "Field[Any]",
    #     proto_type: Literal[ProtoType.ENUM],
    #     *,
    #     number: int,
    #     enum: str,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    # Field("ProtoPlusMessage") -> Any
    # Field("ProtoPlusEnum") -> Any
    #@overload
    # def __init__(
    #     self: "Field[Any]",
    #     proto_type: str,
    #     *,
    #     number: int,
    #     oneof: Optional[str] = None,
    #     json_name: Optional[str] = None,
    #     optional: bool = False,
    # ) -> None: ...
    def __init__(
        self,
        proto_type: Union[ProtoType, Type["Message"], Type[message.Message], Type["Enum"], Type[EnumTypeWrapper], str],
        *,
        number: int,
        message: Optional[Union[Type["Message"], Type[message.Message], str]] = None,
        enum: Optional[Union[Type["Enum"], Type[EnumTypeWrapper], str]] = None,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False
    ):
        # This class is not intended to stand entirely alone;
        # data is augmented by the metaclass for Message.
        self.mcls_data = None
        self.parent = None

        # If the proto type sent is an object or a string, it is really
        # a message or enum.
        if not isinstance(proto_type, int):
            # Note: We only support the "shortcut syntax" for enums
            # when receiving the actual class.
            if isinstance(proto_type, (EnumMeta, EnumTypeWrapper)):
                enum = proto_type
                proto_type = ProtoType.ENUM
            else:
                message = proto_type
                proto_type = ProtoType.MESSAGE

        # Save the direct arguments.
        self.number = number
        self.proto_type = proto_type
        self.message = message
        self.enum = enum
        self.json_name = json_name
        self.optional = optional
        self.oneof = oneof

        # Once the descriptor is accessed the first time, cache it.
        # This is important because in rare cases the message or enum
        # types are written later.
        self._descriptor = None

    @property
    def descriptor(self):
        """Return the descriptor for the field."""
        if not self._descriptor:
            # Resolve the message type, if any, to a string.
            type_name = None
            if isinstance(self.message, str):
                if not self.message.startswith(self.package):
                    self.message = "{package}.{name}".format(
                        package=self.package,
                        name=self.message,
                    )
                type_name = self.message
            elif self.message:
                type_name = (
                    self.message.DESCRIPTOR.full_name
                    if hasattr(self.message, "DESCRIPTOR")
                    else self.message._meta.full_name
                )
            elif isinstance(self.enum, str):
                if not self.enum.startswith(self.package):
                    self.enum = "{package}.{name}".format(
                        package=self.package,
                        name=self.enum,
                    )
                type_name = self.enum
            elif self.enum:
                type_name = (
                    self.enum.DESCRIPTOR.full_name
                    if hasattr(self.enum, "DESCRIPTOR")
                    else self.enum._meta.full_name
                )

            # Set the descriptor.
            self._descriptor = descriptor_pb2.FieldDescriptorProto(
                name=self.name,
                number=self.number,
                label=3 if self.repeated else 1,
                type=self.proto_type,
                type_name=type_name,
                json_name=self.json_name,
                proto3_optional=self.optional,
            )

        # Return the descriptor.
        return self._descriptor

    @property
    def name(self) -> str:
        """Return the name of the field."""
        return self.mcls_data["name"]

    @property
    def package(self) -> str:
        """Return the package of the field."""
        return self.mcls_data["package"]

    @property
    def pb_type(self):
        """Return the composite type of the field, or the primitive type if a primitive."""
        # For enums, return the Python enum.
        if self.enum:
            return self.enum

        # For primitive fields, we still want to know
        # what the type is.
        if not self.message:
            return self.proto_type

        # Return the internal protobuf message.
        if hasattr(self.message, "_meta"):
            return self.message.pb()
        return self.message

    if TYPE_CHECKING:
        # The first one technically only happens for optional fields.
        @overload
        def __get__(self, obj: None, objtype: type["Message"]) -> str: ...
        @overload
        def __get__(self, obj: "Message", objtype: type["Message"]) -> T: ...
        def __get__(self, obj: Optional["Message"], objtype: type["Message"]) -> Union[str, T]: ...


class RepeatedField(Field[T]):
    """A representation of a repeated field in protocol buffers."""

    repeated = True

    @overload
    def __init__(
        self: "RepeatedField[float]",
        proto_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[int]",
        proto_type: IntegerProtoType,
        *,
        number: int,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[bool]",
        proto_type: Literal[ProtoType.BOOL],
        *,
        number: int,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[str]",
        proto_type: Literal[ProtoType.STRING],
        *,
        number: int,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[bytes]",
        proto_type: Literal[ProtoType.BYTES],
        *,
        number: int,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[T]",
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[T],
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[T]",
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[T],
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[T]",
        proto_type: type[T],
        *,
        number: int,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[Any]",
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: "RepeatedField[Any]",
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False,
    ) -> None: ...
    def __init__(
        self,
        proto_type: Union[ProtoType, Type["Message"], Type[message.Message], Type["Enum"], Type[EnumTypeWrapper], str],
        *,
        number: int,
        message: Optional[Union[Type["Message"], Type[message.Message], str]] = None,
        enum: Optional[Union[Type["Enum"], Type[EnumTypeWrapper], str]] = None,
        oneof: Optional[str] = None,
        json_name: Optional[str] = None,
        optional: bool = False
    ) -> None:
        return super().__init__(proto_type, number=number, message=message, enum=enum, oneof=oneof, json_name=json_name, optional=optional)

    if TYPE_CHECKING:
        # The first one technically only happens for optional fields.
        @overload  # type: ignore[override]
        def __get__(self, obj: None, objtype: type["Message"]) -> str: ...
        @overload  # type: ignore[override]
        def __get__(self, obj: "Message", objtype: type["Message"]) -> MutableSequence[T]: ...
        def __get__(self, obj: Optional["Message"], objtype: type["Message"]) -> Union[str, MutableSequence[T]]: ...  # type: ignore[override]


K = TypeVar("K")
V = TypeVar("V")

class MapField(Field[V], Generic[K, V]):
    """A representation of a map field in protocol buffers."""

    @overload
    def __init__(
        self: "MapField[int, float]",
        key_type: IntegerProtoType,
        value_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, int]",
        key_type: IntegerProtoType,
        value_type: IntegerProtoType,
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, bool]",
        key_type: IntegerProtoType,
        value_type: Literal[ProtoType.BOOL],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, str]",
        key_type: IntegerProtoType,
        value_type: Literal[ProtoType.STRING],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, bytes]",
        key_type: IntegerProtoType,
        value_type: Literal[ProtoType.BYTES],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, V]",
        key_type: IntegerProtoType,
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[V],
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, V]",
        key_type: IntegerProtoType,
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[V],
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, V]",
        key_type: IntegerProtoType,
        value_type: type[V],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, Any]",
        key_type: IntegerProtoType,
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[int, Any]",
        key_type: IntegerProtoType,
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, float]",
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, int]",
        key_type: Literal[ProtoType.STRING],
        value_type: IntegerProtoType,
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, bool]",
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.BOOL],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, str]",
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.STRING],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, bytes]",
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.BYTES],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, V]",
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[V],
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, V]",
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[V],
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, V]",
        key_type: Literal[ProtoType.STRING],
        value_type: type[V],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, Any]",
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
    ) -> None: ...
    @overload
    def __init__(
        self: "MapField[str, Any]",
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
    ) -> None: ...
    def __init__(
        self, 
        key_type: Literal[IntegerProtoType, ProtoType.STRING],
        value_type: Union[ProtoType, Type["Message"], Type[message.Message], Type["Enum"], Type[EnumTypeWrapper], str],
        *,
        number: int,
        message: Optional[Union[Type["Message"], Type[message.Message], str]] = None,
        enum: Optional[Union[Type["Enum"], Type[EnumTypeWrapper], str]] = None
    ):
        super().__init__(value_type, number=number, message=message, enum=enum)
        self.map_key_type = key_type

    if TYPE_CHECKING:
        # The first one technically only happens for optional fields.
        @overload  # type: ignore[override]
        def __get__(self, obj: None, objtype: type["Message"]) -> str: ...
        @overload  # type: ignore[override]
        def __get__(self, obj: "Message", objtype: type["Message"]) -> MutableMapping[K, V]: ...
        def __get__(self, obj: Optional["Message"], objtype: type["Message"]) -> Union[str, MutableMapping[K, V]]: ...  # type: ignore[override]


__all__ = (
    "Field",
    "MapField",
    "RepeatedField",
)
