import unittest
from probes import *
from measurement import *

probes= ProbesByAsn('42')

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
        measurement = Measurement(description, target, probes, address_family, resolve_on_probe,
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
        measurement = Measurement(description, target, probes, address_family, resolve_on_probe,
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
        measurement = Measurement(description, target, probes, address_family, resolve_on_probe,
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
        self.failUnlessRaises(ValueError, Measurement, description, target, probes, address_family, 
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
        self.failUnlessRaises(ValueError, Measurement, description, target, probes, address_family, 
                resolve_on_probe, is_oneoff, can_visualise, is_public)

    def testGoodMeasurementPing_1(self):
        '''Test a valid Ping Measurement'''
        description = 'test'
        target = 'test'
        measurement = MeasurementPing(description, target, probes)
        self.assertIsInstance(measurement, MeasurementPing)

    def testBadMeasurementPing_1(self):
        '''Test bad interval'''
        description = 'test'
        target = 'test'
        interval = 0
        self.failUnlessRaises(ValueError, MeasurementPing, description, target, probes, 
                interval=interval)

    def testBadMeasurementPing_2(self):
        '''Test 0 packet count'''
        description = 'test'
        target = 'test'
        packets = 0
        self.failUnlessRaises(ValueError, MeasurementPing, description, target, probes, 
                packets=packets)

    def testBadMeasurementPing_3(self):
        '''Test high packet count'''
        description = 'test'
        target = 'test'
        packets = 17
        self.failUnlessRaises(ValueError, MeasurementPing, description, target, probes, 
                packets=packets)

    def testBadMeasurementPing_4(self):
        '''Test 0 size'''
        description = 'test'
        target = 'test'
        size = 0
        self.failUnlessRaises(ValueError, MeasurementPing, description, target, probes, 
                size=size)

    def testBadMeasurementPing_5(self):
        '''Test high size'''
        description = 'test'
        target = 'test'
        size = 2049
        self.failUnlessRaises(ValueError, MeasurementPing, description, target, probes, 
                size=size)

    def testGoodMeasurementSSL_1(self):
        '''Test a valid SSL Measurement'''
        description = 'test'
        target = 'test'
        measurement = MeasurementSSL(description, target, probes)
        self.assertIsInstance(measurement, MeasurementSSL)

    def testBadMeasurementSSL_1(self):
        '''Test low port'''
        description = 'test'
        target = 'test'
        port = 0
        self.failUnlessRaises(ValueError, MeasurementSSL, description, target, probes, 
                port=port)

    def testBadMeasurementSSL_2(self):
        '''Test high port'''
        description = 'test'
        target = 'test'
        port = 605536
        self.failUnlessRaises(ValueError, MeasurementSSL, description, target, probes, 
                port=port)

    def testGoodMeasurementTraceroute_1(self):
        '''Test a valid Traceroute Measurement'''
        description = 'test'
        target = 'test'
        measurement = MeasurementTraceroute(description, target, probes)
        self.assertIsInstance(measurement, MeasurementTraceroute)

    def testBadMeasurementTraceroute_1(self):
        '''Test bad interval'''
        description = 'test'
        target = 'test'
        interval = 0
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                interval=interval)

    def testBadMeasurementTraceroute_2(self):
        '''Test bad protocol'''
        description = 'test'
        target = 'test'
        protocol = 'TCP'
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                protocol=protocol)

    def testBadMeasurementTraceroute_3(self):
        '''Test 0 paris count'''
        description = 'test'
        target = 'test'
        paris = 0
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                paris=paris)

    def testBadMeasurementTraceroute_4(self):
        '''Test high paris count'''
        description = 'test'
        target = 'test'
        paris = 17
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                paris=paris)

    def testBadMeasurementTraceroute_5(self):
        '''Test 0 firsthop count'''
        description = 'test'
        target = 'test'
        firsthop = 0
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                firsthop=firsthop)

    def testBadMeasurementTraceroute_6(self):
        '''Test high firsthop count'''
        description = 'test'
        target = 'test'
        firsthop = 256
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                firsthop=firsthop)

    def testBadMeasurementTraceroute_7(self):
        '''Test 0 maxhops count'''
        description = 'test'
        target = 'test'
        maxhops = 0
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                maxhops=maxhops)

    def testBadMeasurementTraceroute_8(self):
        '''Test high maxhops count'''
        description = 'test'
        target = 'test'
        maxhops = 256
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                maxhops=maxhops)

    def testBadMeasurementTraceroute_9(self):
        '''Test 0 timeout'''
        description = 'test'
        target = 'test'
        timeout = 0
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                timeout=timeout)

    def testBadMeasurementTraceroute_10(self):
        '''Test high timeout'''
        description = 'test'
        target = 'test'
        timeout = 60001
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                timeout=timeout)

    def testBadMeasurementTraceroute_11(self):
        '''Test 0 size'''
        description = 'test'
        target = 'test'
        size = 0
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                size=size)

    def testBadMeasurementTraceroute_12(self):
        '''Test high size'''
        description = 'test'
        target = 'test'
        size = 2049
        self.failUnlessRaises(ValueError, MeasurementTraceroute, description, target, probes, 
                size=size)


if __name__ == '__main__':
    unittest.main()


