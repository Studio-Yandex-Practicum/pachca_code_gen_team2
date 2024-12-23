from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_chat import QueryChat


T = TypeVar("T", bound="CreateChatBody")


@_attrs_define
class CreateChatBody:
    """
    Attributes:
        chat (Union[Unset, QueryChat]): Собранный объект параметров создаваемой беседы или канала
    """

    chat: Union[Unset, "QueryChat"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chat, Unset):
            chat = self.chat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat is not UNSET:
            field_dict["chat"] = chat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.query_chat import QueryChat

        d = src_dict.copy()
        _chat = d.pop("chat", UNSET)
        chat: Union[Unset, QueryChat]
        if isinstance(_chat, Unset):
            chat = UNSET
        else:
            chat = QueryChat.from_dict(_chat)

        create_chat_body = cls(
            chat=chat,
        )

        create_chat_body.additional_properties = d
        return create_chat_body

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
