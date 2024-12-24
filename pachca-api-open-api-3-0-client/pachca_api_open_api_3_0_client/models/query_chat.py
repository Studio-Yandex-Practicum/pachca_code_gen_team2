from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryChat")


@_attrs_define
class QueryChat:
    """Собранный объект параметров создаваемой беседы или канала

    Attributes:
        name (str): Название Example: 🤿 aqua.
        member_ids (Union[Unset, list[int]]): Массив идентификаторов пользователей, которые станут участниками Example:
            [186, 187].
        channel (Union[Unset, bool]): Тип: беседа (по умолчанию, false) или канал (true) Example: True.
        public (Union[Unset, bool]): Доступ: закрытый (по умолчанию, false) или открытый (true)
    """

    name: str
    member_ids: Union[Unset, list[int]] = UNSET
    channel: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        member_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.member_ids, Unset):
            member_ids = self.member_ids

        channel = self.channel

        public = self.public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if member_ids is not UNSET:
            field_dict["member_ids"] = member_ids
        if channel is not UNSET:
            field_dict["channel"] = channel
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        member_ids = cast(list[int], d.pop("member_ids", UNSET))

        channel = d.pop("channel", UNSET)

        public = d.pop("public", UNSET)

        query_chat = cls(
            name=name,
            member_ids=member_ids,
            channel=channel,
            public=public,
        )

        query_chat.additional_properties = d
        return query_chat

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
