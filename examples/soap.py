import suds

url = "http://tis-oi.dev/api/soap?wsdl"
client = suds.client.Client(url)
print client.service.purchaseService("1162050981", "OISEG2", "WEB")
