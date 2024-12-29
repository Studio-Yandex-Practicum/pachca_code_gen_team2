from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_status_status import QueryStatusStatus


T = TypeVar("T", bound="QueryStatus")


@_attrs_define
class QueryStatus:
    """
    Attributes:
        status (Union[Unset, QueryStatusStatus]): Собранный объект параметров нового статуса
    """

    status: Union[Unset, "QueryStatusStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.query_status_status import QueryStatusStatus

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, QueryStatusStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = QueryStatusStatus.from_dict(_status)

        query_status = cls(
            status=status,
        )

        query_status.additional_properties = d
        return query_status

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
