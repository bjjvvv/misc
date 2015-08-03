import xml.etree.cElementTree as etree

"""bjj
"""

if __name__ == '__main__':
    tree = etree.parse('feed.xml')
    root = tree.getroot()
