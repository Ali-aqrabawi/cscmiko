from .base import BaseConfig, BaseConfigs


class Route(BaseConfig):

    @property
    def is_connected(self):
        return self.protocol == 'C'

    @property
    def is_eigrp(self):
        return self.protocol == 'D'

    @property
    def is_ospf(self):
        return self.protocol == 'O'

    @property
    def is_static(self):
        return self.protocol == 'S'

    @property
    def is_bgp(self):
        return self.protocol == 'B'

    @property
    def is_rip(self):
        return self.protocol == 'R'


class Routes(BaseConfigs):
    model = Route

    @property
    def ospf_list(self):
        return [i for i in self.all if i.is_ospf]

    @property
    def eigrp_list(self):
        return [i for i in self.all if i.is_eigrp]

    @property
    def direct_connected_list(self):
        return [i for i in self.all if i.is_connected]

    @property
    def static_list(self):
        return [i for i in self.all if i.is_static]

    @property
    def rip_list(self):
        return [i for i in self.all if i.is_rip]

    def get_routes_of_next_hope_ip(self, ip):
        return [i for i in self.all if ip == i.nexthop_ip]

    def get_routes_of_next_hope_if(self, interface):
        return [i for i in self.all if interface == i.nexthop_if.lower()]

    def get_routes_of_network(self, network):
        return [i for i in self.all if network == i.network]


class Bgp(BaseConfig):
    @property
    def is_igp_origin(self):
        if self.origin == 'i':
            return True
        return False

    @property
    def is_egp_origin(self):
        if self.origin == 'e':
            return True
        return False

    @property
    def is_incomplete(self):
        if self.origin == '?':
            return True
        return False

    @property
    def is_best(self):
        if self.path_selection == '<':
            return True
        return False

    @property
    def is_valid(self):
        if self.status == '*':
            return True
        return False

    @property
    def is_internal(self):
        if self.route_source == 'i':
            return True
        return False

    @property
    def is_supressed(self):
        if self.status == 's':
            return True
        return False


class BgpNeighbors(BaseConfigs):
    model = Bgp

    @property
    def supressed_list(self):
        return [i for i in self.all if i.is_supressed]

    @property
    def internal_list(self):
        return [i for i in self.all if i.is_internal]

    @property
    def valid_list(self):
        return [i for i in self.all if i.is_valid]

    @property
    def incomplete_list(self):
        return [i for i in self.all if i.is_incomplete]

    @property
    def best_list(self):
        return [i for i in self.all if i.is_best]

    @property
    def egp_list(self):
        return [i for i in self.all if i.is_egp]

    @property
    def igp_list(self):
        return [i for i in self.all if i.is_igp]

    def get_bgp_by_network(self, network):
        for i in self.all:
            if i.network == network:
                return i

class Ospf(BaseConfig):
    pass

class OspfNeighbors(BaseConfigs):
    model = Ospf

class Vrf(BaseConfig):
    pass

class Vrfs(BaseConfigs):
    model = Vrf
