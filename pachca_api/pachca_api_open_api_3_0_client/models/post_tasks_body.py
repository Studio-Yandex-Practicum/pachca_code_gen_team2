from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_tasks_body_task import PostTasksBodyTask


T = TypeVar("T", bound="PostTasksBody")


@_attrs_define
class PostTasksBody:
    """
    Attributes:
        task (Union[Unset, PostTasksBodyTask]):
    """

    task: Union[Unset, "PostTasksBodyTask"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task is not UNSET:
            field_dict["task"] = task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_tasks_body_task import PostTasksBodyTask

        d = src_dict.copy()
        _task = d.pop("task", UNSET)
        task: Union[Unset, PostTasksBodyTask]
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = PostTasksBodyTask.from_dict(_task)

        post_tasks_body = cls(
            task=task,
        )

        post_tasks_body.additional_properties = d
        return post_tasks_body

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
