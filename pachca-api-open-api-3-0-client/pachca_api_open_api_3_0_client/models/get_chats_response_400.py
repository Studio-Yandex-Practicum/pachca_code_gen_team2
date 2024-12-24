from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.errors_code import ErrorsCode


T = TypeVar("T", bound="GetChatsResponse400")


@_attrs_define
class GetChatsResponse400:
    """
    Attributes:
        errors (Union[Unset, ErrorsCode]): Bad Request
    """

    errors: Union[Unset, "ErrorsCode"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.errors_code import ErrorsCode

        d = src_dict.copy()
        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, ErrorsCode]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ErrorsCode.from_dict(_errors)

        get_chats_response_400 = cls(
            errors=errors,
        )

        get_chats_response_400.additional_properties = d
        return get_chats_response_400

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
