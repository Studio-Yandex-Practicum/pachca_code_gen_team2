from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMembersToChatsBody")


@_attrs_define
class PostMembersToChatsBody:
    """
    Attributes:
        member_ids (list[int]):  Example: [186, 187].
        silent (Union[Unset, bool]):
    """

    member_ids: list[int]
    silent: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_ids = self.member_ids

        silent = self.silent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member_ids": member_ids,
            }
        )
        if silent is not UNSET:
            field_dict["silent"] = silent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        member_ids = cast(list[int], d.pop("member_ids"))

        silent = d.pop("silent", UNSET)

        post_members_to_chats_body = cls(
            member_ids=member_ids,
            silent=silent,
        )

        post_members_to_chats_body.additional_properties = d
        return post_members_to_chats_body

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
