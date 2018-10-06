import unittest
import Order
from Order import *


class TestSecurity(unittest.TestCase):
    def test_auth_true(self):
      dealer = Security("1","123")    
      result = Security.Authentication(dealer)
      self.assertEqual(result,'true')
    def test_auth_wrongPwd(self):    
      dealer = Security("1","245")
      result = Security.Authentication(dealer)
      self.assertEqual(result,'false')
    def test_auth_false(self):
      dealer = Security("5","6360")
      result = Security.Authentication(dealer)
      self.assertEqual(result,'false')
    def test_auth_id0(self):
      dealer = Security("0","123")
      result = Security.Authentication(dealer)
      self.assertEqual(result,'false')
    def test_auth_invalid(self):
      dealer = Security("99","XYZ")
      result = Security.Authentication(dealer)
      self.assertEqual(result,'false')
    def test_auth_idngtv(self):
      dealer = Security("-899","XYZ")
      result = Security.Authentication(dealer)
      self.assertEqual(result,'false')
    def test_auth_pwdblank(self):  
      dealer = Security("1","")
      result = Security.Authentication(dealer)
      self.assertEqual(result,'false')
    def test_auth_idblank(self): 
      dealer = Security("","456")
      result = Security.Authentication(dealer)
      self.assertEqual(result,'false')
    def test_auth_idpwdblank(self): 
      dealer = Security("","")
      result = Security.Authentication(dealer)
      self.assertEqual(result,'false')


class TestAddress(unittest.TestCase):
    def test_name(self):
      adddetail = Address("Tom","1333 South Park","Halifax","NS","BTA1A6")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'true')
    def test_street(self):
      adddetail = Address("XXX","1333 South Park","Halifax","NS","BTA1A6")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')
    def test_city(self):
      adddetail = Address("Tom","1333 South Park","XXX","NS","BTA1A6")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')
    def test_province(self):
      adddetail = Address("Tom","1333 South Park","Halifax","XXX","BTA1A6")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')
    def test_postal(self):
      adddetail = Address("Tom","1333 South Park","Halifax","NS","XXX")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')
    def test_name_blank(self):
      adddetail = Address("","1333 South Park","Halifax","NS","BTA1A6")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')
    def test_street_blank(self):   
      adddetail = Address("Tom","","Halifax","NS","BTA1A6")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')
    def test_city_blank(self):   
      adddetail = Address("Tom","1333 South Park","","NS","BTA1A6")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')
    def test_province_blank(self):   
      adddetail = Address("Tom","1333 South Park","Halifax","","BTA1A6")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')
    def test_postal_blank(self):  
      adddetail = Address("Tom","1333 South Park","Halifax","NS","")
      AddressVerified = Address.ValidateAddress(adddetail)
      self.assertEqual(AddressVerified,'false')

  
class TestOrder(unittest.TestCase):
    def test_PartFound(self):
      PartNum = PartManager(11)
      result = PartManager.ValidateOrder(PartNum)
      self.assertEqual(result,'success')
    def test_PartNoLongerSold(self):  
      PartNum = PartManager(999)
      result = PartManager.ValidateOrder(PartNum)
      self.assertNotEqual(result,'success')
    def test_PartOutOfStock(self):
      PartNum = PartManager(111)      
      result = PartManager.ValidateOrder(PartNum)
      self.assertNotEqual(result,'success')
    def test_PartInvalid(self):
      PartNum = PartManager(0)      
      result = PartManager.ValidateOrder(PartNum)
      self.assertNotEqual(result,'success')
    def test_PartNegative(self):
      PartNum = PartManager(-14)      
      result = PartManager.ValidateOrder(PartNum)
      self.assertNotEqual(result,'success')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)