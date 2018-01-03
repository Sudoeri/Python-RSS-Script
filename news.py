#! /usr/bin/env python

import feedparser


print '-----------------------------------------------------'

#Put the title of the news organization you which to retrieve from
print 'The Intercept'

print '-----------------------------------------------------'

#Insert the rss feed URL from your news source
d = feedparser.parse('https://theintercept.com/feed/?lang=en')
#Repeat this for how ever many articles you wish to retrieve
print d['entries'][0]['title'] 

print d.entries[0]['link'] 

print d['entries'][1]['title'] 

print d.entries[1]['link'] 

print d['entries'][2]['title'] 

print d.entries[2]['link'] 

print d['entries'][3]['title'] 

print d.entries[3]['link'] 

print d['entries'][4]['title'] 

print d.entries[4]['link'] 

#Repeat the above with a different news source to retrieve multiple sources at once
