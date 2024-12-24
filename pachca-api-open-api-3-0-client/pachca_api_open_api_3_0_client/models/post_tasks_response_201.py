from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_tasks_response_201_data import PostTasksResponse201Data


T = TypeVar("T", bound="PostTasksResponse201")


@_attrs_define
class PostTasksResponse201:
    """
    Attributes:
        data (Union[Unset, PostTasksResponse201Data]):
    """

    data: Union[Unset, "PostTasksResponse201Data"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_tasks_response_201_data import PostTasksResponse201Data

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PostTasksResponse201Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PostTasksResponse201Data.from_dict(_data)

        post_tasks_response_201 = cls(
            data=data,
        )

        post_tasks_response_201.additional_properties = d
        return post_tasks_response_201

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
