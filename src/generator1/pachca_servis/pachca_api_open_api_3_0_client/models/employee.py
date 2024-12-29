import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_employee_custom_properties_item import BaseEmployeeCustomPropertiesItem
    from ..models.status_type_0 import StatusType0


T = TypeVar("T", bound="Employee")


@_attrs_define
class Employee:
    """
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
        user_status (Union['StatusType0', None, Unset]): Статус. Возвращается как null, если статус не установлен.
        title (Union[Unset, str]): Должность
        created_at (Union[Unset, datetime.datetime]): Дата создания (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ
        time_zone (Union[Unset, str]): Часовой пояс пользователя
        image_url (Union[None, Unset, str]): Ссылка на скачивание аватарки
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
    user_status: Union["StatusType0", None, Unset] = UNSET
    title: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    time_zone: Union[Unset, str] = UNSET
    image_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.status_type_0 import StatusType0

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

        user_status: Union[None, Unset, dict[str, Any]]
        if isinstance(self.user_status, Unset):
            user_status = UNSET
        elif isinstance(self.user_status, StatusType0):
            user_status = self.user_status.to_dict()
        else:
            user_status = self.user_status

        title = self.title

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        time_zone = self.time_zone

        image_url: Union[None, Unset, str]
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

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
        if user_status is not UNSET:
            field_dict["user_status"] = user_status
        if title is not UNSET:
            field_dict["title"] = title
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if image_url is not UNSET:
            field_dict["image_url"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.base_employee_custom_properties_item import BaseEmployeeCustomPropertiesItem
        from ..models.status_type_0 import StatusType0

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

        def _parse_user_status(data: object) -> Union["StatusType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_status_type_0 = StatusType0.from_dict(data)

                return componentsschemas_status_type_0
            except:  # noqa: E722
                pass
            return cast(Union["StatusType0", None, Unset], data)

        user_status = _parse_user_status(d.pop("user_status", UNSET))

        title = d.pop("title", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        time_zone = d.pop("time_zone", UNSET)

        def _parse_image_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_url = _parse_image_url(d.pop("image_url", UNSET))

        employee = cls(
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
            user_status=user_status,
            title=title,
            created_at=created_at,
            time_zone=time_zone,
            image_url=image_url,
        )

        employee.additional_properties = d
        return employee

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
