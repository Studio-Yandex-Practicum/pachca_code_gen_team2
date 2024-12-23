from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_files_item_file_type import MessageFilesItemFileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageFilesItem")


@_attrs_define
class MessageFilesItem:
    """
    Attributes:
        id (Union[Unset, int]):
        key (Union[Unset, str]): Путь к файлу, полученный в результате загрузки файла (каждый файл в каждом сообщении
            должен иметь свой уникальный key, не допускается использование одного и того же key в разных сообщениях)
        name (Union[Unset, str]): Название файла, которое вы хотите отображать пользователю (рекомендуется писать вместе
            с расширением)
        file_type (Union[Unset, MessageFilesItemFileType]):
        url (Union[Unset, str]): Размер файла в байтах, отображаемый пользователю
    """

    id: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    file_type: Union[Unset, MessageFilesItemFileType] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        name = self.name

        file_type: Union[Unset, str] = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if file_type is not UNSET:
            field_dict["file_type"] = file_type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        _file_type = d.pop("file_type", UNSET)
        file_type: Union[Unset, MessageFilesItemFileType]
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = MessageFilesItemFileType(_file_type)

        url = d.pop("url", UNSET)

        message_files_item = cls(
            id=id,
            key=key,
            name=name,
            file_type=file_type,
            url=url,
        )

        message_files_item.additional_properties = d
        return message_files_item

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
