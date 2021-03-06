from typing import TYPE_CHECKING, Optional

from yandex_music import YandexMusicObject

if TYPE_CHECKING:
    from yandex_music import Client


class PersonalPlaylistsData(YandexMusicObject):
    """Класс, представляющий .

    Attributes:
        client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

    Args:
        client (:obj:`yandex_music.Client`, optional): Объект класса :class:`yandex_music.Client`, представляющий клиент
            Yandex Music.
        **kwargs: Произвольные ключевые аргументы полученные от API.
    """

    def __init__(self,
                 is_wizard_passed: bool,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.is_wizard_passed = is_wizard_passed

        self.client = client
        self._id_attrs = (self.is_wizard_passed,)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['PersonalPlaylistsData']:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`yandex_music.PersonalPlaylistsData`: Объект класса :class:`yandex_music.PersonalPlaylistsData`.
        """
        if not data:
            return None

        data = super(PersonalPlaylistsData, cls).de_json(data, client)

        return cls(client=client, **data)
