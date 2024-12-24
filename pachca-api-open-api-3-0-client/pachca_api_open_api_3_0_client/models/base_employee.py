from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_employee_custom_properties_item import BaseEmployeeCustomPropertiesItem


T = TypeVar("T", bound="BaseEmployee")


@_attrs_define
class BaseEmployee:
    """Базовый класс сотрудника.

    Attributes:
        id (Union[Unset, int]): Идентификатор пользователя Example: 1.
        first_name (Union[Unset, str]): Имя
        last_name (Union[Unset, str]): Фамилия
        nickname (Union[Unset, str]): Имя пользователя
        email (Union[Unset, str]): Электронная почта
        phone_number (Union[Unset, str]): Телефон
        department (Union[Unset, str]): Департамент
        role (Union[Unset, str]): Уровень доступа: admin (администратор), user (сотрудник), multi_guest (мульти-гость)
        suspended (Union[Unset, bool]): Деактивация пользователя. При значении true пользователь является
            деактивированным.
        invite_status (Union[Unset, str]): Статус приглашения: confirmed (принято), sent (отправлено)
        list_tags (Union[Unset, list[str]]): Массив тегов, привязанных к сотруднику
        custom_properties (Union[Unset, list['BaseEmployeeCustomPropertiesItem']]): Дополнительные поля сотрудника
        bot (Union[Unset, bool]): Тип: пользователь (false) или бот (true)
    """

    id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    department: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    suspended: Union[Unset, bool] = UNSET
    invite_status: Union[Unset, str] = UNSET
    list_tags: Union[Unset, list[str]] = UNSET
    custom_properties: Union[Unset, list["BaseEmployeeCustomPropertiesItem"]] = UNSET
    bot: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        nickname = self.nickname

        email = self.email

        phone_number = self.phone_number

        department = self.department

        role = self.role

        suspended = self.suspended

        invite_status = self.invite_status

        list_tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.list_tags, Unset):
            list_tags = self.list_tags

        custom_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_properties, Unset):
            custom_properties = []
            for custom_properties_item_data in self.custom_properties:
                custom_properties_item = custom_properties_item_data.to_dict()
                custom_properties.append(custom_properties_item)

        bot = self.bot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if department is not UNSET:
            field_dict["department"] = department
        if role is not UNSET:
            field_dict["role"] = role
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if invite_status is not UNSET:
            field_dict["invite_status"] = invite_status
        if list_tags is not UNSET:
            field_dict["list_tags"] = list_tags
        if custom_properties is not UNSET:
            field_dict["custom_properties"] = custom_properties
        if bot is not UNSET:
            field_dict["bot"] = bot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.base_employee_custom_properties_item import BaseEmployeeCustomPropertiesItem

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        nickname = d.pop("nickname", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        department = d.pop("department", UNSET)

        role = d.pop("role", UNSET)

        suspended = d.pop("suspended", UNSET)

        invite_status = d.pop("invite_status", UNSET)

        list_tags = cast(list[str], d.pop("list_tags", UNSET))

        custom_properties = []
        _custom_properties = d.pop("custom_properties", UNSET)
        for custom_properties_item_data in _custom_properties or []:
            custom_properties_item = BaseEmployeeCustomPropertiesItem.from_dict(custom_properties_item_data)

            custom_properties.append(custom_properties_item)

        bot = d.pop("bot", UNSET)

        base_employee = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            email=email,
            phone_number=phone_number,
            department=department,
            role=role,
            suspended=suspended,
            invite_status=invite_status,
            list_tags=list_tags,
            custom_properties=custom_properties,
            bot=bot,
        )

        base_employee.additional_properties = d
        return base_employee

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
