from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectResponse")


@_attrs_define
class DirectResponse:
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
        file (Union[Unset, str]):
    """

    content_disposition: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    policy: Union[Unset, str] = UNSET
    x_amz_credential: Union[Unset, str] = UNSET
    x_amz_algorithm: Union[Unset, str] = UNSET
    x_amz_date: Union[Unset, str] = UNSET
    x_amz_signature: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    file: Union[Unset, str] = UNSET
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

        file = self.file

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
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        content_disposition = (
            self.content_disposition
            if isinstance(self.content_disposition, Unset)
            else (None, str(self.content_disposition).encode(), "text/plain")
        )

        acl = self.acl if isinstance(self.acl, Unset) else (None, str(self.acl).encode(), "text/plain")

        policy = self.policy if isinstance(self.policy, Unset) else (None, str(self.policy).encode(), "text/plain")

        x_amz_credential = (
            self.x_amz_credential
            if isinstance(self.x_amz_credential, Unset)
            else (None, str(self.x_amz_credential).encode(), "text/plain")
        )

        x_amz_algorithm = (
            self.x_amz_algorithm
            if isinstance(self.x_amz_algorithm, Unset)
            else (None, str(self.x_amz_algorithm).encode(), "text/plain")
        )

        x_amz_date = (
            self.x_amz_date
            if isinstance(self.x_amz_date, Unset)
            else (None, str(self.x_amz_date).encode(), "text/plain")
        )

        x_amz_signature = (
            self.x_amz_signature
            if isinstance(self.x_amz_signature, Unset)
            else (None, str(self.x_amz_signature).encode(), "text/plain")
        )

        key = self.key if isinstance(self.key, Unset) else (None, str(self.key).encode(), "text/plain")

        file = self.file if isinstance(self.file, Unset) else (None, str(self.file).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

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
        if file is not UNSET:
            field_dict["file"] = file

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

        file = d.pop("file", UNSET)

        direct_response = cls(
            content_disposition=content_disposition,
            acl=acl,
            policy=policy,
            x_amz_credential=x_amz_credential,
            x_amz_algorithm=x_amz_algorithm,
            x_amz_date=x_amz_date,
            x_amz_signature=x_amz_signature,
            key=key,
            file=file,
        )

        direct_response.additional_properties = d
        return direct_response

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
