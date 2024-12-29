from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditMessagesButtonsItemItem")


@_attrs_define
class EditMessagesButtonsItemItem:
    """
    Attributes:
        text (Union[Unset, str]): Текст, отображаемый на кнопке пользователю
        url (Union[Unset, str]): Ссылка, которая будет открыта по нажатию кнопки
        data (Union[Unset, str]): Данные, которые будут отправлены в исходящем вебхуке по нажатию кнопки
    """

    text: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        url = self.url

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        url = d.pop("url", UNSET)

        data = d.pop("data", UNSET)

        edit_messages_buttons_item_item = cls(
            text=text,
            url=url,
            data=data,
        )

        edit_messages_buttons_item_item.additional_properties = d
        return edit_messages_buttons_item_item

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
