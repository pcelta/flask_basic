from src.builders.abstract_builder import AbstractBuilder
from src.entities.content import Content
from xml.etree import ElementTree
from configs.loader import Loader

class Builder(AbstractBuilder):

    def build(self, order):

        settings = Loader.get_partner_settings("MCAFEE")

        xml  = ElementTree.Element("PARTNERCONTEXT")

        header = ElementTree.Element("HEADER")

        partner = ElementTree.Element("PARTNER", {"PARTNER_ID" : order["partnerId"]})

        header.append(partner)
        xml.append(header)

        data = ElementTree.Element("DATA")

        customer_context = ElementTree.Element("CUSTOMERCONTEXT", {
            "ID" : order["purchase"],
            "REQUESTTYPE" : settings["ACTIVATE_REQUEST_TYPE"]
        })


        account = ElementTree.Element("ACCOUNT")
        email_address = ElementTree.Element("EMAILADDRESS")
        email_address.text = order["email"]

        first_name = ElementTree.Element("FIRSTNAME")
        first_name.text = order["login"]

        last_name = ElementTree.Element("LASTNAME")
        last_name.text = order["login"]

        password = ElementTree.Element("PASSWORD")
        password.text = order["password"]


        preference = ElementTree.Element("PREFERENCE", {"TYPE" : settings["PREFERENCE_TYPE"]})
        preference.text = order["language"]

        preferences = ElementTree.Element("PREFERENCES")
        preferences.append(preference)

        account.append(email_address)
        account.append(first_name)
        account.append(last_name)
        account.append(password)
        account.append(preferences)

        customer_context.append(account)

        item = ElementTree.Element("ITEM", {
            "SKU"       : order["sku"],
            "QTY"       : settings["ITEM_QTY"],
            "ACTION"    : settings["ACTIVATE_ITEM_ACTION"]
        })
        item.text = "."

        items = ElementTree.Element("ITEMS")
        items.append(item)

        order_element = ElementTree.Element("ORDER", {
            "PARTNERREF"    : order["purchase"],
            "REF"           : settings["ACTIVATE_ORDER_REF"]
        })
        order_element.append(items)
        customer_context.append(order_element)
        data.append(customer_context)

        xml.append(data)
        return Content({"xml" : ElementTree.tostring(xml)})
