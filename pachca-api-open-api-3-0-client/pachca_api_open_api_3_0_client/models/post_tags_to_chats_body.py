from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostTagsToChatsBody")


@_attrs_define
class PostTagsToChatsBody:
    """
    Attributes:
        group_tag_ids (list[int]):  Example: [86, 18].
    """

    group_tag_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_tag_ids = self.group_tag_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_tag_ids": group_tag_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        group_tag_ids = cast(list[int], d.pop("group_tag_ids"))

        post_tags_to_chats_body = cls(
            group_tag_ids=group_tag_ids,
        )

        post_tags_to_chats_body.additional_properties = d
        return post_tags_to_chats_body

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
