from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.errors_code_payload import ErrorsCodePayload


T = TypeVar("T", bound="ErrorsCode")


@_attrs_define
class ErrorsCode:
    """Bad Request

    Attributes:
        key (Union[Unset, str]):
        value (Union[Unset, str]):
        message (Union[Unset, str]):
        code (Union[Unset, str]):
        payload (Union[Unset, ErrorsCodePayload]):
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    payload: Union[Unset, "ErrorsCodePayload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        message = self.message

        code = self.code

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.errors_code_payload import ErrorsCodePayload

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        message = d.pop("message", UNSET)

        code = d.pop("code", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, ErrorsCodePayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ErrorsCodePayload.from_dict(_payload)

        errors_code = cls(
            key=key,
            value=value,
            message=message,
            code=code,
            payload=payload,
        )

        errors_code.additional_properties = d
        return errors_code

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
