import xml.etree.ElementTree as ET
xml_data = ("C://Users//Ved Prakash Shukla//Downloads//test//ck_customers.xml")
ns = {'ns': "http://www.demandware.com/xml/impex/customer/2006-10-31"}
root = ET.parse(xml_data).getroot()
for customer in root.findall("./ns:customer", ns):
    customer_no = customer.get("customer-no")
    customer.set("customer-no", "CK" + customer_no) if customer_no[:2] != "CK" else customer.set("customer-no", customer_no)
tree = ET.ElementTree(root)
tree.write("new_CK.xml")
