import unittest
from probes import Probes

class TestProbes(unittest.TestCase):

    def testGoodAsnPlain(self):
        '''Test a valid ASPLAIN number'''
        value = '1'
        probe_type = 'asn'
        probes = Probes(value, probe_type)
        self.assertIsInstance(probes, Probes)

    def testBadAsnPlain_1(self):
        '''Letters in ASN'''
        value = 'a111'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadAsnPlain_2(self):
        '''ASN to big'''
        value = '4294967297'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadAsnPlain_3(self):
        '''ASN to small'''
        value = '0'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testGoodAsnDot(self):
        '''Test a valid ASDOT number'''
        value = '1.1'
        probe_type = 'asn'
        probes = Probes(value, probe_type)
        self.assertIsInstance(probes, Probes)

    def testBadAsnDot_1(self):
        '''To many dots in AS dot notation'''
        value = '1.1.1'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadAsnDot_2(self):
        '''Low byte contains char'''
        value = 'a.1'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadAsnDot_2(self):
        '''High byte contains char'''
        value = '1.a'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadAsnDot_3(self):
        '''Low byte to big'''
        value = '65537.1'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadAsnDot_4(self):
        '''High byte to big'''
        value = '1.65537'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadAsnDot_5(self):
        '''Low byte to small'''
        value = '0.1'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadAsnDot_6(self):
        '''High byte to small'''
        value = '1.0'
        probe_type = 'asn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testGoodCountry(self):
        '''Test a valid iso country code'''
        value = 'gb'
        probe_type = 'country'
        probes = Probes(value, probe_type)
        self.assertIsInstance(probes, Probes)

    def testBadCountry_1(self):
        '''Test a country code with more then 2 letters'''
        value = 'gbr'
        probe_type = 'country'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadCountry_2(self):
        '''Test an invalid country code'''
        value = 'uk'
        probe_type = 'country'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testGoodMsn(self):
        '''Test a valid msn'''
        value = '1000000'
        probe_type = 'msn'
        probes = Probes(value, probe_type)
        self.assertIsInstance(probes, Probes)

    def testBadMsn_1(self):
        '''Test an msn countaing a char'''
        value = '100000a'
        probe_type = 'msn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadMsn_2(self):
        '''Test an msn less then 1000000'''
        value = '999999'
        probe_type = 'msn'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testGoodProbe(self):
        '''Test a valid probe'''
        value = '1'
        probe_type = 'probes'
        probes = Probes(value, probe_type)
        self.assertIsInstance(probes, Probes)

    def testGoodProbeList(self):
        '''Test a valid probe list'''
        value = '1,2'
        probe_type = 'probes'
        probes = Probes(value, probe_type)
        self.assertIsInstance(probes, Probes)

    def testBadProbe_1(self):
        '''Test a probe id less then 1'''
        value = '0,1'
        probe_type = 'probes'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadProbe_2(self):
        '''Test a probe with chars'''
        value = 'a,1'
        probe_type = 'probes'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadProbe_3(self):
        '''Test a probe list with bad delimiter'''
        value = '2.1'
        probe_type = 'probes'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)


    def testGoodIPv4(self):
        '''Test a valid ipv4 prefix'''
        value = '192.0.2.0/24'
        probe_type = 'prefix'
        probes = Probes(value, probe_type)
        self.assertIsInstance(probes, Probes)

    def testBadIPv4_1(self):
        '''prefix to big'''
        value = '192.0.2.0/33'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv4_2(self):
        '''negative prefix'''
        value = '192.0.2.0/-1'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv4_3(self):
        '''Invalid network'''
        value = '392.0.2.0/24'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv4_4(self):
        '''To many octavis'''
        value = '192.0.2.0.0/24'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv4_4(self):
        '''char in preix length'''
        value = '192.0.2.0.0/a'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testGoodIPv6(self):
        '''Test a valid ipv6 prefix'''
        value = '2001:DB8::/32'
        probe_type = 'prefix'
        probes = Probes(value, probe_type)
        self.assertIsInstance(probes, Probes)

    def testBadIPv6_1(self):
        '''prefix to big'''
        value = '2001:DB8::/129'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv6_2(self):
        '''negative prefix'''
        value = '2001:DB8::/-1'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv6_3(self):
        '''Invalid network'''
        value = 'G001:DB8::/32'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv6_4(self):
        '''Too many octavis'''
        value = '2001:DB8::0:0:0:0:0:0/32'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv6_5(self):
        '''Too much compression'''
        value = '2001:DB8::0::0/32'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)

    def testBadIPv6_6(self):
        '''char in preix length'''
        value = '2001:DB8::/a'
        probe_type = 'prefix'
        self.failUnlessRaises(ValueError, Probes, value, probe_type)


if __name__ == '__main__':
    unittest.main()

