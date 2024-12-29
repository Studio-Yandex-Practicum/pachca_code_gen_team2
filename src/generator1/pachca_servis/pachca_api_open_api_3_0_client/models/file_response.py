from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileResponse")


@_attrs_define
class FileResponse:
    """
    Attributes:
        content_disposition (Union[Unset, str]):
        acl (Union[Unset, str]):
        policy (Union[Unset, str]):
        x_amz_credential (Union[Unset, str]):
        x_amz_algorithm (Union[Unset, str]):
        x_amz_date (Union[Unset, str]):
        x_amz_signature (Union[Unset, str]):
        key (Union[Unset, str]):
        direct_url (Union[Unset, str]):
    """

    content_disposition: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    policy: Union[Unset, str] = UNSET
    x_amz_credential: Union[Unset, str] = UNSET
    x_amz_algorithm: Union[Unset, str] = UNSET
    x_amz_date: Union[Unset, str] = UNSET
    x_amz_signature: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    direct_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_disposition = self.content_disposition

        acl = self.acl

        policy = self.policy

        x_amz_credential = self.x_amz_credential

        x_amz_algorithm = self.x_amz_algorithm

        x_amz_date = self.x_amz_date

        x_amz_signature = self.x_amz_signature

        key = self.key

        direct_url = self.direct_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_disposition is not UNSET:
            field_dict["Content-Disposition"] = content_disposition
        if acl is not UNSET:
            field_dict["acl"] = acl
        if policy is not UNSET:
            field_dict["policy"] = policy
        if x_amz_credential is not UNSET:
            field_dict["x-amz-credential"] = x_amz_credential
        if x_amz_algorithm is not UNSET:
            field_dict["x-amz-algorithm"] = x_amz_algorithm
        if x_amz_date is not UNSET:
            field_dict["x-amz-date"] = x_amz_date
        if x_amz_signature is not UNSET:
            field_dict["x-amz-signature"] = x_amz_signature
        if key is not UNSET:
            field_dict["key"] = key
        if direct_url is not UNSET:
            field_dict["direct_url"] = direct_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        content_disposition = d.pop("Content-Disposition", UNSET)

        acl = d.pop("acl", UNSET)

        policy = d.pop("policy", UNSET)

        x_amz_credential = d.pop("x-amz-credential", UNSET)

        x_amz_algorithm = d.pop("x-amz-algorithm", UNSET)

        x_amz_date = d.pop("x-amz-date", UNSET)

        x_amz_signature = d.pop("x-amz-signature", UNSET)

        key = d.pop("key", UNSET)

        direct_url = d.pop("direct_url", UNSET)

        file_response = cls(
            content_disposition=content_disposition,
            acl=acl,
            policy=policy,
            x_amz_credential=x_amz_credential,
            x_amz_algorithm=x_amz_algorithm,
            x_amz_date=x_amz_date,
            x_amz_signature=x_amz_signature,
            key=key,
            direct_url=direct_url,
        )

        file_response.additional_properties = d
        return file_response

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
