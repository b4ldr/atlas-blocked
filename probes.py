from iso3166 import countries
import socket

class Probes(object):
    '''probe definition used to create a new measuerment'''
    def __init__(self, value, probe_type, requested=1):
        '''initiate the probe object'''
        self.value = value.lower()
        self.probe_type = probe_type
        self.requested = requested
        {
            'asn': self.check_asn,
            'country': self.check_country,
            'msn': self.check_msn,
            'prefix': self.check_prefix,
            'probes': self.check_probes,

        }.get(probe_type)(value)

    def _get_ip_version(self, address):
        '''return the ip version of an address'''
        try:
            socket.inet_pton(socket.AF_INET, address)
            return 4
        except socket.error:
            try:
                socket.inet_pton(socket.AF_INET6, address)
                return 6
            except socket.error:
                raise ValueError('%s is not a valid IP address' % address)

    def check_asn(self, asn):
        '''check the value supplied is a correctly formated asn'''
        
        #check if we have an asn with dot notation.  if so change it to the decimal format
        asn_group = asn.split('.')
        if len(asn_group) == 1:
            try:
                asn = int(asn)
                if asn < 1 or asn > 4294967296:
                    raise ValueError('%s is not a valid ASPLAIN number' % asn)
            except ValueError as e:
                e.args += ('%s is not a valid ASPLAIN number' % asn, )
                raise
        elif len(asn_group) == 2:
            try:
                asn_low = int(asn_group[0])
                asn_high = int(asn_group[1])
            except ValueError as e:
                e.args += ('%s is not a valid asn' % asn, )
                raise
            if asn_low > 0 and asn_low <= 65536 and asn_high > 0 and asn_high <= 65536:
                self.asn = asn_low * 65536 + asn_high
            else:
                raise ValueError('%s is not a valid ASDOT number' % asn)
        else:
            raise ValueError('%s is not a valid ASPLAIN or ASDOT number' % asn)


    def check_country(self, country):
        '''check the value supplied is a correctly formated iso country code'''
        #we only check if the country code is 2 characters not if it is valid
        if len(country) == 2:
            try:
                countries.get(country)
            except KeyError:
                raise ValueError('%s is not a valid iso3166 alpha 2 code' % country)
        else:
            raise ValueError('%s is not a valid iso3166 alpha 2 code' % country)

    def check_msn(self, msn):
        '''check the value supplied is a correctly formated msn id'''
        try:
            msn = int(msn)
            if msn < 1000000:
                raise ValueError('%s is not a valid msn' % msn)
        except ValueError as e:
            e.args += ('%s is not a valid msn' % msn, )
            raise

    def check_prefix(self, prefix):
        '''check the value supplied is a correctly formated prefix'''
        prefix_group = prefix.split('/')
        if len(prefix_group) == 2:
            prefix_length = int(prefix_group[1])
            #check we have a valid ipv4 or ipv6
            version = self._get_ip_version(prefix_group[0])
            try:
                if version == 4:
                    if prefix_length < 0 or prefix_length > 32:
                        raise ValueError('%s is not a valid IPv4 prefix size' % prefix_length)
                elif version == 6:
                    if prefix_length < 0 or prefix_length > 128:
                        raise ValueError('%s is not a valid IPv6 prefix size' % prefix_length)
            except ValueError as e:
                e.args += ('%s is not a valid prefix length' % prefix_length, )
                raise
        else:
            raise ValueError('%s is not a valid prefix' % prefix)

    def check_probes(self, probes):
        '''check the value supplied is a correctly formated probes list'''
        for probe in probes.split(','):
            try:
                if int(probe) < 1:
                    raise ValueError('%s is not a valid probe' % probe)
            except ValueError as e:
                e.args += ('%s is not a valid probe' % probe, )
                raise




