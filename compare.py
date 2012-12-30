import urllib2  # Import urllib2 for downloading the xml.etree
import xml.etree.ElementTree as et  # Import ElementTree for parsing xml.etree
import csv  # For outputting.
import re

xml_url = "http://www.creeperrepo.net/static/FTB2/modpacks.xml"
raw_xml = urllib2.urlopen(xml_url)  # We don't use .read() because et.parse
# Takes a file object.

root = et.parse(raw_xml).getroot()


def normalize(string):
    """Normalizes a string."""
    string = string.lower()  # Lower case

    string = string.replace("'", "")

    regex = re.compile(r" by (.)*")
    string = re.sub(regex, "", string)

    regex = re.compile(r"(\d)+")
    string = re.sub(regex, "", string)

    string = string.replace(" ", "")

    string = string.title()

    return string

mods = []  # Compile a list of all the mods used.
packs = []  # Compile a list of all the packs.
for pack in root:  # For every pack in the mod packs
    packs.append(pack.attrib["name"])
    for mod in pack.attrib["mods"].split("; "):  # For every mod in pack
        mod = normalize(mod)

        if mod not in mods:
            mods.append(mod.replace(" ", "").title())  # Add to known mods.

mods = sorted(mods)  # Sort mods alphabeticly - I spelled alphabeticly wrong
# didn't I. Oh well.

# Write it.
rows = []
rows.append(mods)

for pack in root:
    row = []
    row.append(pack.attrib["name"] + "(%s)" % pack.attrib["mcVersion"])

    for _ in range(1, len(mods)):
        row.append("NO")

    for mod in pack.attrib["mods"].split("; "):
        mod = normalize(mod)

        i = 0
        for compare_mod in rows[0]:
            if mod == compare_mod and i > 0:
                row[i] = "YES"
                print "added %s, i was %s" % (mod, i)
            i += 1
    rows.append(row)


### Credits.
rows.append([])
rows.append(["Made by: Dkkline"])
rows.append(["Source is on my github."])


with open("ftb_compare.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, delimiter="_")
    for row in rows:
        writer.writerow(row)