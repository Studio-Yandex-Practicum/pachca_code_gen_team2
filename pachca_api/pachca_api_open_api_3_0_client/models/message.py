import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_entity_type import MessageEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.button import Button
    from ..models.message_files_item import MessageFilesItem
    from ..models.message_forwarding import MessageForwarding
    from ..models.message_thread import MessageThread


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        entity_type (Union[Unset, MessageEntityType]):  Default: MessageEntityType.DISCUSSION.
        entity_id (Union[Unset, int]):
        content (Union[Unset, str]):
        id (Union[Unset, int]):
        chat_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        files (Union[Unset, list['MessageFilesItem']]):
        buttons (Union[Unset, list[list['Button']]]):
        thread (Union['MessageThread', None, Unset]):
        forwarding (Union['MessageForwarding', None, Unset]):
        parent_message_id (Union[None, Unset, int]): Идентификатор сообщения, к которому написан ответ. Возвращается как
            null, если сообщение не является ответом.
    """

    entity_type: Union[Unset, MessageEntityType] = MessageEntityType.DISCUSSION
    entity_id: Union[Unset, int] = UNSET
    content: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    chat_id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    files: Union[Unset, list["MessageFilesItem"]] = UNSET
    buttons: Union[Unset, list[list["Button"]]] = UNSET
    thread: Union["MessageThread", None, Unset] = UNSET
    forwarding: Union["MessageForwarding", None, Unset] = UNSET
    parent_message_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_forwarding import MessageForwarding
        from ..models.message_thread import MessageThread

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        entity_id = self.entity_id

        content = self.content

        id = self.id

        chat_id = self.chat_id

        user_id = self.user_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

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

        thread: Union[None, Unset, dict[str, Any]]
        if isinstance(self.thread, Unset):
            thread = UNSET
        elif isinstance(self.thread, MessageThread):
            thread = self.thread.to_dict()
        else:
            thread = self.thread

        forwarding: Union[None, Unset, dict[str, Any]]
        if isinstance(self.forwarding, Unset):
            forwarding = UNSET
        elif isinstance(self.forwarding, MessageForwarding):
            forwarding = self.forwarding.to_dict()
        else:
            forwarding = self.forwarding

        parent_message_id: Union[None, Unset, int]
        if isinstance(self.parent_message_id, Unset):
            parent_message_id = UNSET
        else:
            parent_message_id = self.parent_message_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if content is not UNSET:
            field_dict["content"] = content
        if id is not UNSET:
            field_dict["id"] = id
        if chat_id is not UNSET:
            field_dict["chat_id"] = chat_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if files is not UNSET:
            field_dict["files"] = files
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if thread is not UNSET:
            field_dict["thread"] = thread
        if forwarding is not UNSET:
            field_dict["forwarding"] = forwarding
        if parent_message_id is not UNSET:
            field_dict["parent_message_id"] = parent_message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.button import Button
        from ..models.message_files_item import MessageFilesItem
        from ..models.message_forwarding import MessageForwarding
        from ..models.message_thread import MessageThread

        d = src_dict.copy()
        _entity_type = d.pop("entity_type", UNSET)
        entity_type: Union[Unset, MessageEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = MessageEntityType(_entity_type)

        entity_id = d.pop("entity_id", UNSET)

        content = d.pop("content", UNSET)

        id = d.pop("id", UNSET)

        chat_id = d.pop("chat_id", UNSET)

        user_id = d.pop("user_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = MessageFilesItem.from_dict(files_item_data)

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

        def _parse_thread(data: object) -> Union["MessageThread", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                thread_type_0 = MessageThread.from_dict(data)

                return thread_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageThread", None, Unset], data)

        thread = _parse_thread(d.pop("thread", UNSET))

        def _parse_forwarding(data: object) -> Union["MessageForwarding", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                forwarding_type_0 = MessageForwarding.from_dict(data)

                return forwarding_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageForwarding", None, Unset], data)

        forwarding = _parse_forwarding(d.pop("forwarding", UNSET))

        def _parse_parent_message_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_message_id = _parse_parent_message_id(d.pop("parent_message_id", UNSET))

        message = cls(
            entity_type=entity_type,
            entity_id=entity_id,
            content=content,
            id=id,
            chat_id=chat_id,
            user_id=user_id,
            created_at=created_at,
            files=files,
            buttons=buttons,
            thread=thread,
            forwarding=forwarding,
            parent_message_id=parent_message_id,
        )

        message.additional_properties = d
        return message

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
