from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_messages_buttons_item_item import EditMessagesButtonsItemItem
    from ..models.edit_messages_files import EditMessagesFiles


T = TypeVar("T", bound="EditMessages")


@_attrs_define
class EditMessages:
    """Для получения сообщения вам необходимо знать его id и указать его в URL запроса.

    Attributes:
        content (Union[Unset, str]): Текст сообщения Default: 'Текст сообщения'.
        files (Union[Unset, EditMessagesFiles]):
        buttons (Union[Unset, list[list['EditMessagesButtonsItemItem']]]): Массив строк, каждая из которых представлена
            массивом кнопок. Подробнее о том, как формировать строки кнопок и какие есть ограничения вы можете прочитать в
            статье. Для удаления кнопок у сообщения пришлите пустой массив.
    """

    content: Union[Unset, str] = "Текст сообщения"
    files: Union[Unset, "EditMessagesFiles"] = UNSET
    buttons: Union[Unset, list[list["EditMessagesButtonsItemItem"]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        files: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        buttons: Union[Unset, list[list[dict[str, Any]]]] = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = []
                for buttons_item_item_data in buttons_item_data:
                    buttons_item_item = buttons_item_item_data.to_dict()
                    buttons_item.append(buttons_item_item)

                buttons.append(buttons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if files is not UNSET:
            field_dict["files"] = files
        if buttons is not UNSET:
            field_dict["buttons"] = buttons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.edit_messages_buttons_item_item import EditMessagesButtonsItemItem
        from ..models.edit_messages_files import EditMessagesFiles

        d = src_dict.copy()
        content = d.pop("content", UNSET)

        _files = d.pop("files", UNSET)
        files: Union[Unset, EditMessagesFiles]
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = EditMessagesFiles.from_dict(_files)

        buttons = []
        _buttons = d.pop("buttons", UNSET)
        for buttons_item_data in _buttons or []:
            buttons_item = []
            _buttons_item = buttons_item_data
            for buttons_item_item_data in _buttons_item:
                buttons_item_item = EditMessagesButtonsItemItem.from_dict(buttons_item_item_data)

                buttons_item.append(buttons_item_item)

            buttons.append(buttons_item)

        edit_messages = cls(
            content=content,
            files=files,
            buttons=buttons,
        )

        edit_messages.additional_properties = d
        return edit_messages

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
