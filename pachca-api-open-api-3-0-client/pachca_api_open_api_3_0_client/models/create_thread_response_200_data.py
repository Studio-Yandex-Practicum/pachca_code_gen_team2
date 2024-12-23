import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateThreadResponse200Data")


@_attrs_define
class CreateThreadResponse200Data:
    """
    Attributes:
        id (Union[Unset, int]): Идентификатор созданного треда.
        chat_id (Union[Unset, int]): Идентификатор чата треда.
        message_id (Union[Unset, int]): Идентификатор сообщения, к которому был создан тред.
        message_chat_id (Union[Unset, int]): Идентификатор чата сообщения.
        updated_at (Union[Unset, datetime.datetime]): Дата и время обновления треда (ISO-8601, UTC+0) в формате YYYY-MM-
            DDThh:mm:ss.sssZ.
    """

    id: Union[Unset, int] = UNSET
    chat_id: Union[Unset, int] = UNSET
    message_id: Union[Unset, int] = UNSET
    message_chat_id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        chat_id = self.chat_id

        message_id = self.message_id

        message_chat_id = self.message_chat_id

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if chat_id is not UNSET:
            field_dict["chat_id"] = chat_id
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if message_chat_id is not UNSET:
            field_dict["message_chat_id"] = message_chat_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        chat_id = d.pop("chat_id", UNSET)

        message_id = d.pop("message_id", UNSET)

        message_chat_id = d.pop("message_chat_id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        create_thread_response_200_data = cls(
            id=id,
            chat_id=chat_id,
            message_id=message_id,
            message_chat_id=message_chat_id,
            updated_at=updated_at,
        )

        create_thread_response_200_data.additional_properties = d
        return create_thread_response_200_data

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
