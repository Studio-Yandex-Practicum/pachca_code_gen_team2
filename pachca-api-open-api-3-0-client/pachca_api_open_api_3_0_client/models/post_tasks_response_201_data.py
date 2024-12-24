import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_tasks_response_201_data_custom_properties_item import (
        PostTasksResponse201DataCustomPropertiesItem,
    )


T = TypeVar("T", bound="PostTasksResponse201Data")


@_attrs_define
class PostTasksResponse201Data:
    """
    Attributes:
        id (Union[Unset, int]): Идентификатор созданного напоминания
        kind (Union[Unset, str]): Тип
        content (Union[Unset, str]): Описание
        due_at (Union[Unset, datetime.datetime]): Срок выполнения (ISO-8601)
        priority (Union[Unset, int]): Приоритет
        user_id (Union[Unset, int]): Идентификатор пользователя-создателя
        status (Union[Unset, str]): Статус напоминания
        created_at (Union[Unset, datetime.datetime]): Дата и время создания
        performer_ids (Union[Unset, list[int]]):
        custom_properties (Union[Unset, list['PostTasksResponse201DataCustomPropertiesItem']]):
    """

    id: Union[Unset, int] = UNSET
    kind: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    due_at: Union[Unset, datetime.datetime] = UNSET
    priority: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    performer_ids: Union[Unset, list[int]] = UNSET
    custom_properties: Union[Unset, list["PostTasksResponse201DataCustomPropertiesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        content = self.content

        due_at: Union[Unset, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        priority = self.priority

        user_id = self.user_id

        status = self.status

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        performer_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.performer_ids, Unset):
            performer_ids = self.performer_ids

        custom_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_properties, Unset):
            custom_properties = []
            for custom_properties_item_data in self.custom_properties:
                custom_properties_item = custom_properties_item_data.to_dict()
                custom_properties.append(custom_properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if content is not UNSET:
            field_dict["content"] = content
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if priority is not UNSET:
            field_dict["priority"] = priority
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if performer_ids is not UNSET:
            field_dict["performer_ids"] = performer_ids
        if custom_properties is not UNSET:
            field_dict["custom_properties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_tasks_response_201_data_custom_properties_item import (
            PostTasksResponse201DataCustomPropertiesItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        content = d.pop("content", UNSET)

        _due_at = d.pop("due_at", UNSET)
        due_at: Union[Unset, datetime.datetime]
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at)

        priority = d.pop("priority", UNSET)

        user_id = d.pop("user_id", UNSET)

        status = d.pop("status", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        performer_ids = cast(list[int], d.pop("performer_ids", UNSET))

        custom_properties = []
        _custom_properties = d.pop("custom_properties", UNSET)
        for custom_properties_item_data in _custom_properties or []:
            custom_properties_item = PostTasksResponse201DataCustomPropertiesItem.from_dict(custom_properties_item_data)

            custom_properties.append(custom_properties_item)

        post_tasks_response_201_data = cls(
            id=id,
            kind=kind,
            content=content,
            due_at=due_at,
            priority=priority,
            user_id=user_id,
            status=status,
            created_at=created_at,
            performer_ids=performer_ids,
            custom_properties=custom_properties,
        )

        post_tasks_response_201_data.additional_properties = d
        return post_tasks_response_201_data

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
