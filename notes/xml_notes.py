### xml is one universal way of storing data
### xml is more complex relative to JSON
### it is similar to html as that it has tags.

### Has start tags and end tags, end tags have the slash
### <person></person>
### In xml, the tags can be anything
### They can also have attributes, like type, or hide
###     <phone type="intl">
### Can also have self closing tags
### Think of XML as a tree, has nodes and tags can be within
### tags. We can also think of it like paths or folders to a 
### to a directory.

### XML document should go through a validator to 
### make sure it is in the correct format. The XML
### schema contract is XML that is a little more complex
### XSD outlines what the XML document can look like
### YYYY-MM-DD  HH:MM:SS
### In the contract have things such as minOccurs, maxOccurs,
### type, name, etc.

import xml.etree.ElementTree as ET
### Triple quoted string is a multiple line string
data =''' <person>
        <name>Nicholas</name>
        <phone type="intl>
            +1 206 519 2002
        </phone>
        <email hide="yes"/>
    </person>'''
tree = ET.fromstring(data)
### Gets the text between the tag name
print('Name:', tree.find('name').text)
### Get's what the attirbute is set to for hide in the email tag
print('Attr:', tree.find('email').get('hide'))

input = '''<stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Nicholas</name>
            </user>
            <user x="7">
                <id>002</id>
                <name>Nathan</name>
            </user>
        </users>
    </stuff>'''
stuff = ET.fromstring(input)
### Finds all the user tags in users
lst = stuff.findall('users/user')
print('User count:', len(lst))
### Iterates through each user tag
for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute', item.get("x"))
