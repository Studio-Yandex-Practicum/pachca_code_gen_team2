from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_messages import EditMessages


T = TypeVar("T", bound="PutMessagesIdBody")


@_attrs_define
class PutMessagesIdBody:
    """
    Attributes:
        message (Union[Unset, EditMessages]): Для получения сообщения вам необходимо знать его id и указать его в URL
            запроса.
    """

    message: Union[Unset, "EditMessages"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.edit_messages import EditMessages

        d = src_dict.copy()
        _message = d.pop("message", UNSET)
        message: Union[Unset, EditMessages]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = EditMessages.from_dict(_message)

        put_messages_id_body = cls(
            message=message,
        )

        put_messages_id_body.additional_properties = d
        return put_messages_id_body

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
