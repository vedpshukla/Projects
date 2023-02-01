import xml.etree.ElementTree as ET

CK_file = ("C://Users//Ved Prakash Shukla//Downloads//Python_Scripts//new_ckk31.xml")
HH_file = ("C://Users//Ved Prakash Shukla//Downloads//Python_Scripts//new_hhh31.xml")
Allheart_file = ("C://Users//Ved Prakash Shukla//Downloads//Python_Scripts//allheartt31.xml")


def update_allheart(CK_file, HH_file, Allheart_file):
    # parse xml files
    CK_tree = ET.parse(CK_file)
    HH_tree = ET.parse(HH_file)
    Allheart_tree = ET.parse(Allheart_file)

    # create a set to store the login ids
    login_ids = set()

    # get the root element for each xml file
    CK_root = CK_tree.getroot()
    HH_root = HH_tree.getroot()
    Allheart_root = Allheart_tree.getroot()

    # create a namespace dictionary for easy access to elements
    ns = {'ns': 'http://www.demandware.com/xml/impex/customer/2006-10-31'}

    # loop through all customers in the CK xml file
    for customer in CK_root.findall("./ns:customer", ns):
        # get the login id
        login = customer.find("./ns:credentials/ns:login", ns).text

        # if the login id is not already in the set of login ids
        if login not in login_ids:
            # add the customer to the Allheart xml file
            Allheart_root.append(customer)
            # add the login id to the set of login ids
            login_ids.add(login)

    # loop through all customers in the HH xml file
    for customer in HH_root.findall("./ns:customer", ns):
        # get the login id
        login = customer.find("./ns:credentials/ns:login", ns).text

        # if the login id is not already in the set of login ids
        if login not in login_ids:
            # add the customer to the Allheart xml file
            Allheart_root.append(customer)
            # add the login id to the set of login ids
            login_ids.add(login)

    # write the updated Allheart xml file
    Allheart_tree.write("Allheartt31.xml")


# example usage
update_allheart("new_ckk31.xml", "new_hhh31.xml", "Allheartt31.xml")