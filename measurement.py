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

    def __init__(self, description, target, address_family=4, resolve_on_probe=True, 
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

    def __init__(self, description, target, address_family=4, resolve_on_probe=True, 
            is_oneoff=True, can_visualise=True, is_public=True,
            interval=240, packets=3, size=1):
            super(MeasurementPing, self).__init__(description, target, address_family, 
                    resolve_on_probe, is_oneoff, can_visualise, is_public)
            self.interval = _cast('interval', interval, int)
            if self.interval < 1:
                raise ValueError('interval ({}) must be a positive int'.format(self.interval))
            self.packets = _cast('packets', packets, int)

            if self.packets < 1 or self.packets > 16:
                raise ValueError('packets ({}) must be between 1 and 16'.format(self.packets))

            self.size = _cast('size', size, int)
            if self.size < 1 or self.size > 2048:
                raise ValueError('size ({}) must be between 1 and 2048'.format(self.size))
        
