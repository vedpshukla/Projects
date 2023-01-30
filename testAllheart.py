import xml.etree.ElementTree as ET

CK_file=("C://Users//Ved Prakash Shukla//Downloads//ck.xml")
HH_file=("C://Users//Ved Prakash Shukla//Downloads//hh.xml")
Allheart_file=("C://Users//Ved Prakash Shukla//Downloads//allheart.xml")

ns = {"ns": "http://www.demandware.com/xml/impex/customer/2006-10-31"}

def update_allheart(CK_file, HH_file, Allheart_file):
    # parse CK.xml
    CK_tree = ET.parse(CK_file)
    CK_root = CK_tree.getroot()

    # parse HH.xml
    HH_tree = ET.parse(HH_file)
    HH_root = HH_tree.getroot()

    # parse Allheart.xml
    Allheart_tree = ET.parse(Allheart_file)
    Allheart_root = Allheart_tree.getroot()

    # store the login ids in a set for quick look-up
    login_ids = set()
    for customer in Allheart_root.findall("./ns:customer", ns):
        login = customer.find("./ns:credentials/ns:login", ns).text
        login_ids.add(login)

    # add the customers from CK.xml
    for customer in CK_root.findall("./ns:customer", ns):
        login = customer.find("./ns:credentials/ns:login", ns).text
        if login not in login_ids:
            Allheart_root.append(customer)
            login_ids.add(login)
        else:
            for existing_customer in Allheart_root.findall("./ns:customer", ns):
                existing_login = existing_customer.find("./ns:credentials/ns:login", ns).text
                if existing_login == login:
                    Allheart_root.remove(existing_customer)
                    Allheart_root.append(customer)
                    break

    # add the customers from HH.xml
    for customer in HH_root.findall("./ns:customer", ns):
        login = customer.find("./ns:credentials/ns:login", ns).text
        if login not in login_ids:
            Allheart_root.append(customer)
            login_ids.add(login)
        else:
            for existing_customer in Allheart_root.findall("./ns:customer", ns):
                existing_login = existing_customer.find("./ns:credentials/ns:login", ns).text
                if existing_login == login:
                    Allheart_root.remove(existing_customer)
                    Allheart_root.append(customer)
                    break

    # write the updated Allheart.xml
    Allheart_tree.write("Allheart_updated.xml")

# example usage
update_allheart("CK.xml", "HH.xml", "Allheart.xml")
