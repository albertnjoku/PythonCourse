#!/usr/bin/env python2
import feedparser as fp

# parse YouTube playlist named 'Popular Fails'
rss = fp.parse('https://www.youtube.com/feeds/videos.xml?channel_id=UCBcRF18a7Qf58cCRy5xuWwQ')

# print number of entries in feed
print('total entries:'+str(len(rss.entries)))

# print publish dates, video links
for i in rss.entries:
    print(i)
    print('published:', i['published'][0:10]) # print date published
    print('video url:', i['link'])
    print('video id:', i['yt_videoid'])
    print('title:', i['title'])
    print('author:', i['author'])
    print('updated:', i['updated'][0:10]) # print date published
    print('media_thumbnail:', i['media_thumbnail'])
    print('summary:', i['summary'])

    StarRating = {}
    '''
    for rating in i.media_starrating:
        StarRating.update(rating)
        print(StarRating['count'])
        print(StarRating['average'])
        print(StarRating['min'])
        print(StarRating['max'])
    '''
    d = {}
    for j in i.links:
        d.update(j)  # add URLs to dictionary
    print(d['href']) # print URLs