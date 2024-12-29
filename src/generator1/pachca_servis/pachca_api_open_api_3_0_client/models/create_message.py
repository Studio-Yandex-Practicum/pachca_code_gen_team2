from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_message_entity_type import CreateMessageEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.button import Button
    from ..models.create_message_files_item import CreateMessageFilesItem


T = TypeVar("T", bound="CreateMessage")


@_attrs_define
class CreateMessage:
    """
    Attributes:
        entity_id (int):
        content (str):
        entity_type (Union[Unset, CreateMessageEntityType]):  Default: CreateMessageEntityType.DISCUSSION.
        files (Union[Unset, list['CreateMessageFilesItem']]):
        buttons (Union[Unset, list[list['Button']]]):
        parent_message_id (Union[None, Unset, int]):
        skip_invite_mentions (Union[Unset, bool]):  Default: False.
        link_preview (Union[Unset, bool]):  Default: False.
    """

    entity_id: int
    content: str
    entity_type: Union[Unset, CreateMessageEntityType] = CreateMessageEntityType.DISCUSSION
    files: Union[Unset, list["CreateMessageFilesItem"]] = UNSET
    buttons: Union[Unset, list[list["Button"]]] = UNSET
    parent_message_id: Union[None, Unset, int] = UNSET
    skip_invite_mentions: Union[Unset, bool] = False
    link_preview: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        content = self.content

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        buttons: Union[Unset, list[list[dict[str, Any]]]] = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for componentsschemas_buttons_item_data in self.buttons:
                componentsschemas_buttons_item = []
                for componentsschemas_buttons_item_item_data in componentsschemas_buttons_item_data:
                    componentsschemas_buttons_item_item = componentsschemas_buttons_item_item_data.to_dict()
                    componentsschemas_buttons_item.append(componentsschemas_buttons_item_item)

                buttons.append(componentsschemas_buttons_item)

        parent_message_id: Union[None, Unset, int]
        if isinstance(self.parent_message_id, Unset):
            parent_message_id = UNSET
        else:
            parent_message_id = self.parent_message_id

        skip_invite_mentions = self.skip_invite_mentions

        link_preview = self.link_preview

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_id": entity_id,
                "content": content,
            }
        )
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if files is not UNSET:
            field_dict["files"] = files
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if parent_message_id is not UNSET:
            field_dict["parent_message_id"] = parent_message_id
        if skip_invite_mentions is not UNSET:
            field_dict["skip_invite_mentions"] = skip_invite_mentions
        if link_preview is not UNSET:
            field_dict["link_preview"] = link_preview

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.button import Button
        from ..models.create_message_files_item import CreateMessageFilesItem

        d = src_dict.copy()
        entity_id = d.pop("entity_id")

        content = d.pop("content")

        _entity_type = d.pop("entity_type", UNSET)
        entity_type: Union[Unset, CreateMessageEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = CreateMessageEntityType(_entity_type)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = CreateMessageFilesItem.from_dict(files_item_data)

            files.append(files_item)

        buttons = []
        _buttons = d.pop("buttons", UNSET)
        for componentsschemas_buttons_item_data in _buttons or []:
            componentsschemas_buttons_item = []
            _componentsschemas_buttons_item = componentsschemas_buttons_item_data
            for componentsschemas_buttons_item_item_data in _componentsschemas_buttons_item:
                componentsschemas_buttons_item_item = Button.from_dict(componentsschemas_buttons_item_item_data)

                componentsschemas_buttons_item.append(componentsschemas_buttons_item_item)

            buttons.append(componentsschemas_buttons_item)

        def _parse_parent_message_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_message_id = _parse_parent_message_id(d.pop("parent_message_id", UNSET))

        skip_invite_mentions = d.pop("skip_invite_mentions", UNSET)

        link_preview = d.pop("link_preview", UNSET)

        create_message = cls(
            entity_id=entity_id,
            content=content,
            entity_type=entity_type,
            files=files,
            buttons=buttons,
            parent_message_id=parent_message_id,
            skip_invite_mentions=skip_invite_mentions,
            link_preview=link_preview,
        )

        create_message.additional_properties = d
        return create_message

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
