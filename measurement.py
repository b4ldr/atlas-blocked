from probes import Probes

def _cast(name, value, cast_type):
    '''intelegent cast function with nicer messages'''
    if cast_type == bool:
        if type(value) == bool:
            return value
        elif value in ['True', 'true', '1', 1]:
            return True
        elif value in ['False', 'false', '0', 0]:
            return False
        else:
            raise ValueError('{} must be {}'.format(name, cast_type) )
    try:
        return cast_type(value)
    except ValueError as e:
        e.args += ('{} must be {}'.format(name, cast_type), )
        raise

class Measurement(object):
    '''new measuerment class'''

    def __init__(self, description, target, probes, address_family=4, resolve_on_probe=True, 
            is_oneoff=True, can_visualise=True, is_public=True):
            self.description = _cast('description', description, str).lower()
            self.target = _cast('target', target, str).lower()
            self.address_family = _cast('address_family', address_family, int)
            if self.address_family not in [4 , 6]:
                raise ValueError('{} invalid address_family, must be 4 or 6'.format(self.address_family))
            self.resolve_on_probe = _cast('resolve_on_probe', resolve_on_probe, bool)
            self.is_oneoff = _cast('is_oneoff', is_oneoff, bool)
            self.can_visualise = _cast('can_visualise', can_visualise, bool)
            self.is_public = _cast('is_public', is_public, bool)

class MeasurementPing(Measurement):
    '''Ping measuerment class'''

    def __init__(self, description, target, probes, address_family=4, resolve_on_probe=True, 
            is_oneoff=True, can_visualise=True, is_public=True,
            interval=240, packets=3, size=1):
            super(MeasurementPing, self).__init__(description, target, probes, address_family, 
                    resolve_on_probe, is_oneoff, can_visualise, is_public)

            self.interval = _cast('interval', interval, int)
            self.packets = _cast('packets', packets, int)
            self.size = _cast('size', size, int)

            if self.interval < 1:
                raise ValueError('interval ({}) must be a positive int'.format(self.interval))

            if self.packets < 1 or self.packets > 16:
                raise ValueError('packets ({}) must be between 1 and 16'.format(self.packets))

            if self.size < 1 or self.size > 2048:
                raise ValueError('size ({}) must be between 1 and 2048'.format(self.size))
        
class MeasurementTraceroute(Measurement):
    '''Traceroute measuerment class'''

    def __init__(self, description, target, probes, address_family=4, resolve_on_probe=True, 
            is_oneoff=True, can_visualise=True, is_public=True,
            interval=900, protocol='ICMP', dontfrag=False, paris=16, firsthop=1, maxhops=32, 
            timeout=4000, size=40):
            super(MeasurementTraceroute, self).__init__(description, target, probes, address_family, 
                    resolve_on_probe, is_oneoff, can_visualise, is_public)

            self.interval = _cast('interval', interval, int)
            self.protocol = _cast('protocol', protocol, str)
            self.dontfrag = _cast('dontfrag', dontfrag, bool)
            self.firsthop = _cast('firsthop', firsthop, int)
            self.maxhops = _cast('maxhops', maxhops, int)
            self.timeout = _cast('timeout', timeout, int)
            self.size = _cast('size', size, int)

            if paris != None:
                print paris
                self.paris = _cast('paris', paris, int)
                if self.paris < 1 or self.paris > 16:
                    raise ValueError('paris ({}) must be between 1 and 16'.format(self.paris))

            if self.interval < 1:
                raise ValueError('interval ({}) must be a positive int'.format(self.interval))

            if self.protocol not in ['ICMP', 'UDP']:
                raise ValueError('protocol ({}) must be ICMP or UDP'.format(self.protocol))

            if self.firsthop < 1 or self.firsthop > 255:
                raise ValueError('firsthop ({}) must be between 1 and 255'.format(self.firsthop))
        
            if self.maxhops < 1 or self.maxhops > 255:
                raise ValueError('maxhops ({}) must be between 1 and 255'.format(self.maxhops))
        
            if self.timeout < 1 or self.timeout > 60000:
                raise ValueError('timeout ({}) must be between 1 and 60000'.format(self.timeout))
        
            if self.size < 1 or self.size > 2048:
                raise ValueError('size ({}) must be between 1 and 2048'.format(self.size))
        
class MeasurementSSL(Measurement):
    '''SSL measuerment class'''

    def __init__(self, description, target, probes, address_family=4, resolve_on_probe=True, 
            is_oneoff=True, can_visualise=True, is_public=True, 
            port=443):
            super(MeasurementSSL, self).__init__(description, target, probes, address_family, 
                    resolve_on_probe, is_oneoff, can_visualise, is_public)

            self.port = _cast('port', port, int)

            if self.port < 1 or self.port > 65535:
                raise ValueError('invalid port ({})'.format(self.port))

