import unittest
from measurement import *

class TestMeasurement(unittest.TestCase):

    def testGoodMeasurement_1(self):
        '''Test a valid Measurement'''
        description = 'test'
        target = 'test'
        address_family = 4
        resolve_on_probe = True
        is_oneoff = True
        can_visualise = True
        is_public = True
        measurement = Measurement(description, target, address_family, resolve_on_probe,
            is_oneoff, can_visualise, is_public)
        self.assertIsInstance(measurement, Measurement)

    def testGoodMeasurement_2(self):
        '''Test a valid Measurement string bools'''
        description = 'test'
        target = 'test'
        address_family = 4
        resolve_on_probe = 'True'
        is_oneoff = 'true'
        can_visualise = 'False'
        is_public = 'false'
        measurement = Measurement(description, target, address_family, resolve_on_probe,
            is_oneoff, can_visualise, is_public)
        self.assertIsInstance(measurement, Measurement)

    def testGoodMeasurement_3(self):
        '''Test a valid Measurement int bools'''
        description = 'test'
        target = 'test'
        address_family = 4
        resolve_on_probe = '1'
        is_oneoff = 1
        can_visualise = '0'
        is_public = 0
        measurement = Measurement(description, target, address_family, resolve_on_probe,
            is_oneoff, can_visualise, is_public)
        self.assertIsInstance(measurement, Measurement)

    def testBadMeasurement_1(self):
        '''Test invalid bool type'''
        description = 'test'
        target = 'test'
        address_family = 'four'
        resolve_on_probe = True
        is_oneoff = True
        can_visualise = True
        is_public = True
        self.failUnlessRaises(ValueError, Measurement, description, target, address_family, 
                resolve_on_probe, is_oneoff, can_visualise, is_public)

    def testBadMeasurement_2(self):
        '''Test invalid address family'''
        description = 'test'
        target = 'test'
        address_family = 5
        resolve_on_probe = True
        is_oneoff = True
        can_visualise = True
        is_public = True
        self.failUnlessRaises(ValueError, Measurement, description, target, address_family, 
                resolve_on_probe, is_oneoff, can_visualise, is_public)

    def testGoodMeasurementPing_1(self):
        '''Test a valid Ping Measurement'''
        description = 'test'
        target = 'test'
        address_family = 4
        resolve_on_probe = True
        is_oneoff = True
        can_visualise = True
        is_public = True
        interval=240
        packets=3
        size=1
        measurement = MeasurementPing(description, target, address_family, resolve_on_probe,
            is_oneoff, can_visualise, is_public, interval, packets, size)
        self.assertIsInstance(measurement, MeasurementPing)

if __name__ == '__main__':
    unittest.main()

