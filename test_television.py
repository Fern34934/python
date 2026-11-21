import pytest
from television import Television


class TestTelevision:
    def setup_method(self) -> None:
        self.tv = Television()

    def teardown_method(self) -> None:
        del self.tv

    def test_init(self) -> None:
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self) -> None:
        self.tv.power()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'
        self.tv.power()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self) -> None:
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'
        self.tv.mute()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 1'
        self.tv.power()
        self.tv.mute()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 1'
        self.tv.mute()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self) -> None:
        self.tv.channel_up()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == 'Power = True, Channel = 1, Volume = 0'
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self) -> None:
        self.tv.channel_down()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self) -> None:
        self.tv.volume_up()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 1'
        self.tv.mute()
        self.tv.volume_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 2'
        self.tv.volume_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self) -> None:
        self.tv.volume_down()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 1'
        self.tv.mute()
        self.tv.volume_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'
        self.tv.volume_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'
