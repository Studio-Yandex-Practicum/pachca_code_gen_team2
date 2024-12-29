from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageForwarding")


@_attrs_define
class MessageForwarding:
    """
    Attributes:
        original_message_id (Union[Unset, int]): Идентификатор оригинального сообщения
        original_chat_id (Union[Unset, int]): Идентификатор чата, в котором находится оригинальное сообщение
        author_id (Union[Unset, int]): Идентификатор чата, в котором находится оригинальное сообщение
        original_created_at (Union[Unset, int]): Дата и время создания оригинального сообщения (ISO-8601, UTC+0) в
            формате YYYY-MM-DDThh:mm:ss.sssZ
        original_thread_id (Union[None, Unset, int]): Идентификатор треда, в котором находится оригинальное сообщение.
            Возвращается как null, если оригинальное сообщение не является комментарием в треде.
        original_thread_message_id (Union[None, Unset, int]): Идентификатор сообщения, к которому был создан тред, в
            котором находится оригинальное сообщение. Возвращается как null, если оригинальное сообщение не является
            комментарием в треде.
        original_thread_parent_chat_id (Union[None, Unset, int]): Идентификатор чата сообщения, к которому был создан
            тред, в котором находится оригинальное сообщение. Возвращается как null, если оригинальное сообщение не является
            комментарием в треде.
    """

    original_message_id: Union[Unset, int] = UNSET
    original_chat_id: Union[Unset, int] = UNSET
    author_id: Union[Unset, int] = UNSET
    original_created_at: Union[Unset, int] = UNSET
    original_thread_id: Union[None, Unset, int] = UNSET
    original_thread_message_id: Union[None, Unset, int] = UNSET
    original_thread_parent_chat_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_message_id = self.original_message_id

        original_chat_id = self.original_chat_id

        author_id = self.author_id

        original_created_at = self.original_created_at

        original_thread_id: Union[None, Unset, int]
        if isinstance(self.original_thread_id, Unset):
            original_thread_id = UNSET
        else:
            original_thread_id = self.original_thread_id

        original_thread_message_id: Union[None, Unset, int]
        if isinstance(self.original_thread_message_id, Unset):
            original_thread_message_id = UNSET
        else:
            original_thread_message_id = self.original_thread_message_id

        original_thread_parent_chat_id: Union[None, Unset, int]
        if isinstance(self.original_thread_parent_chat_id, Unset):
            original_thread_parent_chat_id = UNSET
        else:
            original_thread_parent_chat_id = self.original_thread_parent_chat_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_message_id is not UNSET:
            field_dict["original_message_id"] = original_message_id
        if original_chat_id is not UNSET:
            field_dict["original_chat_id"] = original_chat_id
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if original_created_at is not UNSET:
            field_dict["original_created_at"] = original_created_at
        if original_thread_id is not UNSET:
            field_dict["original_thread_id"] = original_thread_id
        if original_thread_message_id is not UNSET:
            field_dict["original_thread_message_id"] = original_thread_message_id
        if original_thread_parent_chat_id is not UNSET:
            field_dict["original_thread_parent_chat_id"] = original_thread_parent_chat_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        original_message_id = d.pop("original_message_id", UNSET)

        original_chat_id = d.pop("original_chat_id", UNSET)

        author_id = d.pop("author_id", UNSET)

        original_created_at = d.pop("original_created_at", UNSET)

        def _parse_original_thread_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        original_thread_id = _parse_original_thread_id(d.pop("original_thread_id", UNSET))

        def _parse_original_thread_message_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        original_thread_message_id = _parse_original_thread_message_id(d.pop("original_thread_message_id", UNSET))

        def _parse_original_thread_parent_chat_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        original_thread_parent_chat_id = _parse_original_thread_parent_chat_id(
            d.pop("original_thread_parent_chat_id", UNSET)
        )

        message_forwarding = cls(
            original_message_id=original_message_id,
            original_chat_id=original_chat_id,
            author_id=author_id,
            original_created_at=original_created_at,
            original_thread_id=original_thread_id,
            original_thread_message_id=original_thread_message_id,
            original_thread_parent_chat_id=original_thread_parent_chat_id,
        )

        message_forwarding.additional_properties = d
        return message_forwarding

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
