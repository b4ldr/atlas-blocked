import unittest
from probes import *

class TestProbesBy(unittest.TestCase):

    def testGoodAsnPlain(self):
        '''Test a valid ASPLAIN number'''
        value = '1'
        probes = ProbesByAsn(value)
        self.assertIsInstance(probes, ProbesByAsn)

    def testBadAsnPlain_1(self):
        '''Letters in ASN'''
        value = 'a111'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testBadAsnPlain_2(self):
        '''ASN to big'''
        value = '4294967297'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testBadAsnPlain_3(self):
        '''ASN to small'''
        value = '0'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testGoodAsnDot(self):
        '''Test a valid ASDOT number'''
        value = '1.1'
        probes = ProbesByAsn(value)
        self.assertIsInstance(probes, ProbesByAsn)

    def testBadAsnDot_1(self):
        '''To many dots in AS dot notation'''
        value = '1.1.1'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testBadAsnDot_2(self):
        '''Low byte contains char'''
        value = 'a.1'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testBadAsnDot_2(self):
        '''High byte contains char'''
        value = '1.a'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testBadAsnDot_3(self):
        '''Low byte to big'''
        value = '65537.1'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testBadAsnDot_4(self):
        '''High byte to big'''
        value = '1.65537'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testBadAsnDot_5(self):
        '''Low byte to small'''
        value = '0.1'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testBadAsnDot_6(self):
        '''High byte to small'''
        value = '1.0'
        self.failUnlessRaises(ValueError, ProbesByAsn, value)

    def testGoodCountry(self):
        '''Test a valid iso country code'''
        value = 'gb'
        probes = ProbesByCountry(value)
        self.assertIsInstance(probes, ProbesByCountry)

    def testBadCountry_1(self):
        '''Test a country code with more then 2 letters'''
        value = 'gbr'
        self.failUnlessRaises(ValueError, ProbesByCountry, value)

    def testBadCountry_2(self):
        '''Test an invalid country code'''
        value = 'uk'
        self.failUnlessRaises(ValueError, ProbesByCountry, value)

    def testGoodMsn(self):
        '''Test a valid msn'''
        value = '1000000'
        probes = ProbesByMsn(value)
        self.assertIsInstance(probes, ProbesByMsn)

    def testBadMsn_1(self):
        '''Test an msn countaing a char'''
        value = '100000a'
        self.failUnlessRaises(ValueError, ProbesByMsn, value)

    def testBadMsn_2(self):
        '''Test an msn less then 1000000'''
        value = '999999'
        self.failUnlessRaises(ValueError, ProbesByMsn, value)

    def testGoodProbe(self):
        '''Test a valid probe'''
        value = '1'
        probes = ProbesByProbeID(value)
        self.assertIsInstance(probes, ProbesByProbeID)

    def testGoodProbeList(self):
        '''Test a valid probe list'''
        value = '1,2'
        probes = ProbesByProbeID(value)
        self.assertIsInstance(probes, ProbesByProbeID)

    def testBadProbe_1(self):
        '''Test a probe id less then 1'''
        value = '0,1'
        self.failUnlessRaises(ValueError, ProbesByProbeID, value)

    def testBadProbe_2(self):
        '''Test a probe with chars'''
        value = 'a,1'
        self.failUnlessRaises(ValueError, ProbesByProbeID, value)

    def testBadProbe_3(self):
        '''Test a probe list with bad delimiter'''
        value = '2.1'
        self.failUnlessRaises(ValueError, ProbesByProbeID, value)


    def testGoodIPv4(self):
        '''Test a valid ipv4 prefix'''
        value = '192.0.2.0/24'
        probes = ProbesByPrefix(value)
        self.assertIsInstance(probes, ProbesByPrefix)

    def testBadIPv4_1(self):
        '''prefix to big'''
        value = '192.0.2.0/33'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv4_2(self):
        '''negative prefix'''
        value = '192.0.2.0/-1'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv4_3(self):
        '''Invalid network'''
        value = '392.0.2.0/24'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv4_4(self):
        '''To many octavis'''
        value = '192.0.2.0.0/24'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv4_4(self):
        '''char in preix length'''
        value = '192.0.2.0.0/a'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testGoodIPv6(self):
        '''Test a valid ipv6 prefix'''
        value = '2001:DB8::/32'
        probes = ProbesByPrefix(value)
        self.assertIsInstance(probes, ProbesByPrefix)

    def testBadIPv6_1(self):
        '''prefix to big'''
        value = '2001:DB8::/129'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv6_2(self):
        '''negative prefix'''
        value = '2001:DB8::/-1'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv6_3(self):
        '''Invalid network'''
        value = 'G001:DB8::/32'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv6_4(self):
        '''Too many octavis'''
        value = '2001:DB8::0:0:0:0:0:0/32'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv6_5(self):
        '''Too much compression'''
        value = '2001:DB8::0::0/32'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)

    def testBadIPv6_6(self):
        '''char in preix length'''
        value = '2001:DB8::/a'
        self.failUnlessRaises(ValueError, ProbesByPrefix, value)


if __name__ == '__main__':
    unittest.main()

