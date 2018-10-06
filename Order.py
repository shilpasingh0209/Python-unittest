import xml.etree.ElementTree as ET
tree = ET.parse('orderinput.xml')
root = tree.getroot()
class Security:
    def __init__(self,dealerid,dealerkey):
        self.dealerid=dealerid
        self.dealerkey=dealerkey
    def Authentication(self):
        bool='false'

        if(self.dealerid==root[0][0].text and self.dealerkey==root[0][1].text):
            bool='true'

        #Generate Failure XML if dealer is not authorized
        if(bool is not 'true'):
            print("Authorization Failed")
            order = ET.Element("order")
            ET.SubElement(order, "result").text = "failure"
            ET.SubElement(order, "error").text = "Not authorized"
            tree = ET.ElementTree(order)
            tree.write("AuthFailed.xml")
            return bool
        else:
            print("Authorization Successfull")
            return bool

class Address:
    def __init__(self,name,street,city,province,postal):
        self.name=name
        self.street=street
        self.city=city
        self.province=province        
        self.postal=postal
        
    def ValidateAddress(self):
        bool=0
        
        if(str(root[2][0].text)==self.name and str(root[2][1].text)==self.street and str(root[2][2].text)==self.city and str(root[2][3].text)==self.province and str(root[2][4].text)==self.postal):
            bool='true'
            
        if(bool is not 'true'):
            print("******")
            print("Invalid Address")
            order = ET.Element("order")
            ET.SubElement(order, "result").text = "Failure"
            ET.SubElement(order, "error").text = "Invalid Order"
            ET.SubElement(order, "errormessage").text = "Invalid delivery address"
            tree = ET.ElementTree(order)
            tree.write("invalidorder.xml")
            return 'false'
        else:
            print("******")
            print("Address Validated")
            return 'true'

class PartManager:
    def __init__(self,partnum):
        self.partnum=partnum

    def ValidateOrder(self):
        n=root[1].__len__()
        print("n",n)
        order = ET.Element("order")
        orderitems = ET.SubElement(order,"orderitems")
        for i in range(0,n):
            msg=""
            print("******")
            print("ITEM NUMBER",i+1)
            item = ET.SubElement(orderitems, "item")
                #PartNumber
            if(self.partnum==int(root[1][i][0].text) and int(root[1][i][1].text)>0):
              print("Valid")
              ET.SubElement(item, "partnumber").text = str(self.partnum)
              ET.SubElement(item, "quantity").text = root[1][i][1].text
              ET.SubElement(item, "result").text = "success"
              ET.SubElement(item, "errormessage").text = ' '
              msg="success"
            elif(int(root[1][i][0].text)==777):
               print("Out of Stock")
               ET.SubElement(item, "partnumber").text = root[1][i][0].text
               ET.SubElement(item, "quantity").text = root[1][i][1].text
               ET.SubElement(item, "result").text = "failure"
               ET.SubElement(item, "errormessage").text = "out of stock"
               msg="out of stock"
            elif(int(root[1][i][0].text)==999):
              print("No longer Sold")
              ET.SubElement(item, "partnumber").text = root[1][i][0].text
              ET.SubElement(item, "quantity").text = root[1][i][1].text
              ET.SubElement(item, "result").text = "failure"
              ET.SubElement(item, "errormessage").text = "no longer sold"
              msg="no longer sold"
            else:
              print("Not Found")
              ET.SubElement(item, "partnumber").text = root[1][i][0].text
              ET.SubElement(item, "quantity").text = root[1][i][1].text
              ET.SubElement(item, "result").text = "failure"
              ET.SubElement(item, "errormessage").text = "not found"
              msg="not found"
        tree = ET.ElementTree(order)
        tree.write("success.xml")
        return msg

dealer = Security("1","123")
ValidDealer = Security.Authentication(dealer)
print("ValidDealer",ValidDealer)
if(ValidDealer is 'true'):
    adddetail = Address("Tom","1333 South Park","Halifax","NS","BTA1A6")
    AddressVerified = Address.ValidateAddress(adddetail)
    print("AddressVerified",AddressVerified)
    if(AddressVerified is 'true'):
      ValidPart = PartManager(11)
      message = PartManager.ValidateOrder(ValidPart)
      print(message)
