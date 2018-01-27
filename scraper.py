# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://uk.soccerway.com/teams/england/chelsea-football-club/661/")
#
#create an empty dictionary variable to hold our data later
record = {}

root = lxml.html.fromstring(html)
trs = root.cssselect("tr")
for tr in trs:
  divs = tr.cssselect("td div")
  print "Length is {}".format(len(divs))
  print "Name is {}".format(divs[0])
  print "Age is {}".format(divs[1])
  print "We don't care about {}".format(divs[2])
  print "The second name is {}".format(divs[3])
  print "The second age is {}".format(divs[4])
  print "We don't care about {}".format(divs[5])
  # for div in divs:
  #     print "This div is: {}".format(div.text_content().encode('ascii', 'ignore'))
      
      # print div.text_content()  # This is the same as: print "{}".format(div.text_content())
  # names = root.cssselect("td div a")
  # if section = root.cssselect("td div a")
  # print section.text.encode('ascii', 'ignore')
  # print section.attrib['href']

# # Find something on the page using css selectors
#root = lxml.html.fromstring(html)
#names = root.cssselect("td div a")
#for name in names:
 # print name.text
  #print name.text.encode('ascii', 'ignore')
  #print name.attrib['href']
  #store the link in the variable 'record' under the key 'link'
  #record['link'] = name.attrib['href']
  #record['name'] = name.text.encode('ascii', 'ignore')
  #print record
  #scraperwiki.sqlite.save(unique_keys=['link'], data=record)
  

  

# tds = root.cssselect("td div")
# print 'THESE ARE THE TDS', tds
# print 'THERE ARE', len(tds), 'TDS'
#for td in tds:
# div = td.text_content().encode('ascii','ignore')
# if "years" in div:
 # print div
  #record['age'] = div
  #scraperwiki.sqlite.save(unique_keys=['age'], data=record, table_name="ages")


  
  #store the link in the variable 'record' under the key 'link'
  #record['link'] = name.attrib['href']
  #record['name'] = name.text.encode('ascii', 'ignore')
 # print record
 # scraperwiki.sqlite.save(unique_keys=['link'], data=record)
  
  
#print ages
#for age in ages:
 #div = age.text_content().encode('ascii','ignore')
# if "years" in div:
  #print age.text.encode('ascii', 'ignore')
#record['ages'] = name.text.encode('ascii', 'ignore')
#print record
  
  
                      
                          
                          
  
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
