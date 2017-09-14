from xml.parsers.expat import ParserCreate
from collections import deque, OrderedDict
from datetime import datetime
import re

class MySaxHandler(object):

    def __init__(self):
        self.raw_data = OrderedDict()
        self.element = deque()

    def start_element(self, name, attrs):
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        self.element.appendleft(str(name))
        self.parse_attrs(attrs)

    def end_element(self, name):
        #print('sax:end_element: %s' % name)
        self.element.popleft()

    def char_data(self, text):
        #print('sax:char_data: %s' % text)
        if not (text == ''):
            self.raw_data[self.element[0]] = text

    def parse_attrs(self, attrs):
        ele = self.element[0]
        self.raw_data[ele] = dict()
        for key in attrs:
            self.raw_data[ele][key] = attrs[key]

    def raw_data2data(self):
        #today = self.raw_data['']
        pass

handler = MySaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data


xml = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''

parser.Parse(xml)
print(handler.raw_data)