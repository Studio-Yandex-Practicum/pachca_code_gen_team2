import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_tasks_body_task_custom_properties_item import PostTasksBodyTaskCustomPropertiesItem


T = TypeVar("T", bound="PostTasksBodyTask")


@_attrs_define
class PostTasksBodyTask:
    """
    Attributes:
        kind (str): Тип напоминания (call, meeting, reminder, event, email)
        content (str): Описание напоминания
        due_at (datetime.datetime): Срок выполнения напоминания (ISO-8601)
        priority (Union[Unset, int]): Приоритет (1 - по умолчанию, 2 - важно, 3 - очень важно)
        performer_ids (Union[Unset, list[int]]): Массив идентификаторов пользователей
        custom_properties (Union[Unset, list['PostTasksBodyTaskCustomPropertiesItem']]):
    """

    kind: str
    content: str
    due_at: datetime.datetime
    priority: Union[Unset, int] = UNSET
    performer_ids: Union[Unset, list[int]] = UNSET
    custom_properties: Union[Unset, list["PostTasksBodyTaskCustomPropertiesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        content = self.content

        due_at = self.due_at.isoformat()

        priority = self.priority

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
        field_dict.update(
            {
                "kind": kind,
                "content": content,
                "due_at": due_at,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if performer_ids is not UNSET:
            field_dict["performer_ids"] = performer_ids
        if custom_properties is not UNSET:
            field_dict["custom_properties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_tasks_body_task_custom_properties_item import PostTasksBodyTaskCustomPropertiesItem

        d = src_dict.copy()
        kind = d.pop("kind")

        content = d.pop("content")

        due_at = isoparse(d.pop("due_at"))

        priority = d.pop("priority", UNSET)

        performer_ids = cast(list[int], d.pop("performer_ids", UNSET))

        custom_properties = []
        _custom_properties = d.pop("custom_properties", UNSET)
        for custom_properties_item_data in _custom_properties or []:
            custom_properties_item = PostTasksBodyTaskCustomPropertiesItem.from_dict(custom_properties_item_data)

            custom_properties.append(custom_properties_item)

        post_tasks_body_task = cls(
            kind=kind,
            content=content,
            due_at=due_at,
            priority=priority,
            performer_ids=performer_ids,
            custom_properties=custom_properties,
        )

        post_tasks_body_task.additional_properties = d
        return post_tasks_body_task

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
