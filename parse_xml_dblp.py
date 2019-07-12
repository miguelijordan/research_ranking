from gzip import GzipFile
import xmltodict

XML_FILE2 = 'dblp-2019-06-02.xml'
XML_FILE = 'dblp-2019-06-02.xml.gz'

counter = 1

def handle_entry(tag, entry):
    global counter

    if tag[1][0] == 'article':
        print("Tag: " + str(tag))
        print("Entry: " + str(entry))
        print("-------")

    return True


if __name__ == '__main__':
    xmltodict.parse(GzipFile(XML_FILE), item_depth=2, item_callback=handle_entry)
    print("Total: " + str(counter))
