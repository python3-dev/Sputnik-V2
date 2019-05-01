Sputnik V2 is an automated social media manager for your brand. Written in Python 2.7, it fetches updates from multiple RSS feeds, it intearacts with the Twitter API and publish them one by one in Twitter.
# How to use Sputnik V2?
Sputnik V2 can be made functional in a few straightforward and simple steps. Ensure that a stable Python 2.7 enviornment and required libraries are installed prior to these steps.
## Setting up author-Twitter handle database and linking it
Create a CSV file with the byline of authors and the corresponding Twitter handles. Open the file 'TwitterHandles.py'. In line number 13, replace 'handles.csv' with this new filename. Save 'TwitterHandles.py'.
## Setting up Twitter credentials
Apply for a dev account from https://dev.twitter.com/ and get the stuff filled in 'TwitterConf.py'. Save it after editing.
## Setting up the RSS feeds
Open the file 'mainConf.py'. Go to line 9. If you have to add two new RSS feeds: https://www.example.website.com/rss.xml & https://www.another.example.website.com/rss.xml, change the line 9 as follows.

'''
feed_dict = {"E" : "https://www.newsclick.in/rss.xml", "B": "https://www.example.website.com/rss.xml", "C": "https://www.another.example.website.com/rss.xml"}
'''

The strings "E", "B", "C" is abitrarily chosen. It can be anything of your choice. You will only have to ensure that the feeds are in the format <"random_string": "feed_URL">. Each of them must be separated using commas and enclosed in curly brackets {}.

You can also alter the tweet_interval from the default value of 600 seconds to a new value. But it is recommended that this variable is untouched. Using a very small tweet_interval will result in rate limiting errors from Twitter API.
## Running the code
Sputnik V2 is made to run on its own until it is interrupted. To run it in the foreground invoke the Python interpreter as follows, from the folder containing the code.

'''
python main.py
'''

If you want it to run the Python script in the background, issue the following in the terminal.

'''
nohup python main.py &
'''

If all the configurations are correct Tweets will get published at an interval of 600 seconds or whatever is set as long as the RSS feeds are populated and/or the code is running.
