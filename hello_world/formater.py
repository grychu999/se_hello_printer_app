import json
from lxml import etree

PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = 'xml'


SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON, XML]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    elif format == XML:
        result = format_to_xml(msg, imie)
    return result



def format_to_json(msg, imie):
    x = {
        "imie": imie,
        "msg": msg
        }
    return json.dumps(x)


# def format_to_json(msg, imie):
#     return ('{ "imie":"' + imie + '", "mgs":"' +
#              msg + '"}')


def format_to_xml(msg, imie):
    head = etree.Element("gretings")
    etree.SubElement(head, "name").text =imie
    etree.SubElement(head, "msg").text =msg
    return (etree.tostring(head, pretty_print=True).decode('utf-8'))


# def format_to_xml(msg, imie):
#     return ('<greetings>\n'
#     + '<name>' + imie + '</name>\n'
#     + '<msg>' + msg + '</msg>\n'
#     +  '</greetings>\n')



def plain_text(msg, imie):
    return imie + ' ' + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
