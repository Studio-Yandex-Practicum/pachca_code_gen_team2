from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTasksResponse201DataCustomPropertiesItem")


@_attrs_define
class PostTasksResponse201DataCustomPropertiesItem:
    """
    Attributes:
        id (Union[Unset, int]): Идентификатор поля
        name (Union[Unset, str]): Название поля
        data_type (Union[Unset, str]): Тип поля (string, number, date или link)
        value (Union[Unset, str]): Значение
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    data_type: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        data_type = self.data_type

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        data_type = d.pop("data_type", UNSET)

        value = d.pop("value", UNSET)

        post_tasks_response_201_data_custom_properties_item = cls(
            id=id,
            name=name,
            data_type=data_type,
            value=value,
        )

        post_tasks_response_201_data_custom_properties_item.additional_properties = d
        return post_tasks_response_201_data_custom_properties_item

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
