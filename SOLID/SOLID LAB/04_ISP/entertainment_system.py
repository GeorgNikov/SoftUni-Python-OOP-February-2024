class EntertainmentDevice:

    def connect_device_to_power_outlet(self, device):
        pass


class ConnectRCA:
    def connect_rca(self, device):
        pass


class ConnectHDMI:
    def connect_hdmi(self, device):
        pass


class ConnectEthernet:
    def connect_ethernet(self, device):
        pass


class Television(EntertainmentDevice, ConnectRCA, ConnectHDMI):
    def connect_to_dvd(self, dvd_player):
        super().connect_rca(dvd_player)

    def connect_to_game_console(self, game_console):
        super().connect_hdmi(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, ConnectHDMI):
    def connect_to_tv(self, television):
        super().connect_hdmi(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, ConnectHDMI, ConnectEthernet):
    def connect_to_tv(self, television):
        super().connect_hdmi(television)

    def connect_to_router(self, router):
        super().connect_ethernet(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, ConnectEthernet):
    def connect_to_tv(self, television):
        super().connect_ethernet(television)

    def connect_to_game_console(self, game_console):
        super().connect_ethernet(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
