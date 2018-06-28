# worksinprogress
Projects I have worked on for my own research and activity automation in the minneapolis music scene



These files use Python and the Selenium Webdriver. The documentation and download for Selenium can be found here: https://www.seleniumhq.org/projects/webdriver/, and the documentation and download for the chromedriver program I use to allow Selenium to work in the Google Chrome browser can be found here: https://sites.google.com/a/chromium.org/chromedriver/home.




MY FILES

The "'Sota-Pop Facebook Event Info and Data Tracker.py" file is simply a beginning of the second phase of the following file, which is a scraper for Facebook events that will report certain data on the event, like RSVP data (how many users mark "interested" or "going"). The Data Tracker file is simply starting figuring out a method for saving excel sheets to a folder with names by date the data was pulled, so that once fully implemented, it could be used to track Facebook event RSVP data monthly, weekly, daily, or even hourly to see when Minnesotans are most active in their responding to events -- this could inform the operator the best times of day or week to advertise events in order to spend less money and have stronger ROI.

"'Sota-Pop Facebook Page URL Event Scrubber.py" is the workhorse of this repository. It includes definitions for many tasks for the webdriver, including some extraneous ones that were used in the past or may be used in the future. In it's current state, it is set up to fetch data for all of The Dakota Jazz Club's event on Facebook. But it stands for expansion to fetch data for many pages instead of only one, giving the ability to monitor the perfoormance of all of a city's venues' events, in a given time or over a period of time. The output gives the event url,  the event title, number of users marked going and interested, the date of the event, and the url of the venue (though at the moment this seems to be broken). 
  ex. output:
    https://www.facebook.com/events/342689392886796 , The Bacon Brothers at the Dakota , 22 Going · 325 Interested , Friday, July 13 at 7:00 PM - 10:00 PM CDT , None

The two files with the titles "Follow follwers..." are basically scrapers to search around soundcloud for user profiles that are from Minnesota. The need for this program arises because Soundcloud does not allow any easy way to search for many profiles all belonging to a location, and even with the limited options they do provide, not every user actually lists their location. This proggram starts with a profile that is a Minnesotan artists and goes through the profile's followers, checking each for keywords like "MPLS" that would hint to their being a resident or fan of the state, even without a location tag.
