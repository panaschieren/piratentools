#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2012 panaschieren <at> gmx <dot> de

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import codecs
import urllib
from BeautifulSoup import BeautifulSoup

seperator_internal = "&sep;"
seperator_external = " "
my_url = "http://wiki.piratenpartei.de/Mitglieder"
my_in_file = "test.html"
my_out_file = "Mitglieder.csv"

def unesc_seperator(me):
    me = me.replace(seperator_internal,seperator_external)
    return me

def main():
    source_file  = urllib.urlopen(my_url)
    #source_file = codecs.open(my_in_file, encoding='utf-8')
    soup = BeautifulSoup(source_file)
    source_file.close()
    table = soup.find('table', 'wikitable sortable')
    f = codecs.open(my_out_file, encoding='utf-8', mode='w+')
    header="Landesverband&sep;Mitglieder&sep;stimmberechtigt&sep;Mio_Einw&sep;Mitgl_per_Einw&sep;Flaeche&sep;Mitgl_per_kqm&sep;Stand\n"
    f.write(unesc_seperator(header))
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        item = ""
        for td in cols:
          if td.find('b'):#finde Bundesland 
             try:
                   item = item +  td.find('a').string
             except AttributeError:
                   pass
          else:
             item = item + td.find(text=True)
             item = item.strip()
             item = item.replace(" ","_")# "Ausserhalb Deutschlands"
          item = item  + seperator_internal

        if len(item) > 0:
           item = item.rstrip(seperator_internal)
           item = unesc_seperator(item)
           f.write(item + "\n")
           item = ""
    f.close




if __name__ == '__main__':
    main()
