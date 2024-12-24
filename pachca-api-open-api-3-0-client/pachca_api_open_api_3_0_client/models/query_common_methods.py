from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryCommonMethods")


@_attrs_define
class QueryCommonMethods:
    """получение списка актульных полей сущности.

    Attributes:
        id (Union[Unset, int]): Название поля Example: 1.
        name (Union[Unset, str]): Идентификатор поля Example: Дата рождения.
        data_type (Union[Unset, str]): тип поля (string, number, date или link) Example: number.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    data_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        data_type = self.data_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if data_type is not UNSET:
            field_dict["data_type"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        data_type = d.pop("data_type", UNSET)

        query_common_methods = cls(
            id=id,
            name=name,
            data_type=data_type,
        )

        query_common_methods.additional_properties = d
        return query_common_methods

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
