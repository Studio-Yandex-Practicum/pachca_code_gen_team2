from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_message_files_item_file_type import CreateMessageFilesItemFileType

T = TypeVar("T", bound="CreateMessageFilesItem")


@_attrs_define
class CreateMessageFilesItem:
    """
    Attributes:
        key (str):
        name (str):
        file_type (CreateMessageFilesItemFileType):
        size (int):
    """

    key: str
    name: str
    file_type: CreateMessageFilesItemFileType
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        file_type = self.file_type.value

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "file_type": file_type,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        name = d.pop("name")

        file_type = CreateMessageFilesItemFileType(d.pop("file_type"))

        size = d.pop("size")

        create_message_files_item = cls(
            key=key,
            name=name,
            file_type=file_type,
            size=size,
        )

        create_message_files_item.additional_properties = d
        return create_message_files_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
