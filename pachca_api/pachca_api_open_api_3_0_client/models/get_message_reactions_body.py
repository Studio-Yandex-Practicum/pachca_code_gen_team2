from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMessageReactionsBody")


@_attrs_define
class GetMessageReactionsBody:
    """
    Attributes:
        per (Union[Unset, int]): Количество возвращаемых сущностей за один запрос (по умолчанию 50, максимум 50).
            Default: 50.
        page (Union[Unset, int]): Номер страницы выборки (по умолчанию 1). Default: 1.
    """

    per: Union[Unset, int] = 50
    page: Union[Unset, int] = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per = self.per

        page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if per is not UNSET:
            field_dict["per"] = per
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        per = d.pop("per", UNSET)

        page = d.pop("page", UNSET)

        get_message_reactions_body = cls(
            per=per,
            page=page,
        )

        get_message_reactions_body.additional_properties = d
        return get_message_reactions_body

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
