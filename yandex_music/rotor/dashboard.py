from typing import TYPE_CHECKING, Optional, List

from yandex_music import YandexMusicObject

if TYPE_CHECKING:
    from yandex_music import Client, StationResult


class Dashboard(YandexMusicObject):
    """Класс, представляющий рекомендованные станций пользователя.

    Attributes:
        dashboard_id (:obj:`str`): Уникальный идентификатор панели.
        stations (:obj:`list` из :obj:`yandex_music.StationResult`): Список объектов класса
            :class:`yandex_music.StationResult`, представляющих станции со всеми возможными настройками и параметрами.
        pumpkin (:obj:`str`): Хэллоуин.
        client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

    Args:
        dashboard_id (:obj:`str`): Уникальный идентификатор панели.
        stations (:obj:`list` из :obj:`yandex_music.StationResult`): Список объектов класса
            :class:`yandex_music.StationResult`, представляющих станции со всеми возможными настройками и параметрами.
        pumpkin (:obj:`str`): Хэллоуин.
        client (:obj:`yandex_music.Client`, optional): Объект класса :class:`yandex_music.Client`, представляющий клиент
            Yandex Music.
        **kwargs: Произвольные ключевые аргументы полученные от API.
    """

    def __init__(self,
                 dashboard_id: str,
                 stations: List['StationResult'],
                 pumpkin: bool,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.dashboard_id = dashboard_id
        self.stations = stations
        self.pumpkin = pumpkin

        self.client = client
        self._id_attrs = (self.dashboard_id, self.stations, self.pumpkin)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['Dashboard']:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`yandex_music.Dashboard`: Объект класса :class:`yandex_music.Dashboard`.
        """
        if not data:
            return None

        data = super(Dashboard, cls).de_json(data, client)
        from yandex_music import StationResult
        data['stations'] = StationResult.de_list(data.get('stations'), client)

        return cls(client=client, **data)
