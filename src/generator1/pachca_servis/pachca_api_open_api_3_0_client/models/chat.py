import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Chat")


@_attrs_define
class Chat:
    """Беседа или канал

    Attributes:
        id (Union[Unset, int]): Идентификатор беседы или канала Example: 334.
        name (Union[Unset, str]): Название Example: 🤿 aqua.
        owner_id (Union[Unset, int]): Идентификатор пользователя, создавшего беседу или канал Example: 185.
        created_at (Union[Unset, datetime.datetime]): Дата и время создания беседы или канала (ISO-8601, UTC+0) в
            формате YYYY-MM-DDThh:mm:ss.sssZ Example: 2021-08-28T15:56:53.000Z.
        member_ids (Union[Unset, list[int]]): Массив идентификаторов пользователей, участников Example: [185, 186, 187].
        group_tag_ids (Union[Unset, list[int]]): Массив идентификаторов тегов, участников
        channel (Union[Unset, bool]): Тип: беседа (false) или канал (true) Example: True.
        public (Union[Unset, bool]): Доступ: закрытый (false) или открытый (true)
        last_message_at (Union[Unset, datetime.datetime]): Дата и время создания последнего сообщения в беседе/канале
            (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ Example: 2021-08-28T15:58:13.000Z.
        meet_room_url (Union[Unset, str]): Ссылка на Видеочат Example: https://meet.pachca.com/aqua-94bb21b5.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    member_ids: Union[Unset, list[int]] = UNSET
    group_tag_ids: Union[Unset, list[int]] = UNSET
    channel: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    last_message_at: Union[Unset, datetime.datetime] = UNSET
    meet_room_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner_id = self.owner_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        member_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.member_ids, Unset):
            member_ids = self.member_ids

        group_tag_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.group_tag_ids, Unset):
            group_tag_ids = self.group_tag_ids

        channel = self.channel

        public = self.public

        last_message_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_message_at, Unset):
            last_message_at = self.last_message_at.isoformat()

        meet_room_url = self.meet_room_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if member_ids is not UNSET:
            field_dict["member_ids"] = member_ids
        if group_tag_ids is not UNSET:
            field_dict["group_tag_ids"] = group_tag_ids
        if channel is not UNSET:
            field_dict["channel"] = channel
        if public is not UNSET:
            field_dict["public"] = public
        if last_message_at is not UNSET:
            field_dict["last_message_at"] = last_message_at
        if meet_room_url is not UNSET:
            field_dict["meet_room_url"] = meet_room_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        member_ids = cast(list[int], d.pop("member_ids", UNSET))

        group_tag_ids = cast(list[int], d.pop("group_tag_ids", UNSET))

        channel = d.pop("channel", UNSET)

        public = d.pop("public", UNSET)

        _last_message_at = d.pop("last_message_at", UNSET)
        last_message_at: Union[Unset, datetime.datetime]
        if isinstance(_last_message_at, Unset):
            last_message_at = UNSET
        else:
            last_message_at = isoparse(_last_message_at)

        meet_room_url = d.pop("meet_room_url", UNSET)

        chat = cls(
            id=id,
            name=name,
            owner_id=owner_id,
            created_at=created_at,
            member_ids=member_ids,
            group_tag_ids=group_tag_ids,
            channel=channel,
            public=public,
            last_message_at=last_message_at,
            meet_room_url=meet_room_url,
        )

        chat.additional_properties = d
        return chat

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
