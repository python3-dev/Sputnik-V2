Sputnik V2 automates content delivery from your website to Twitter and Telegram. Written in Python 3, it can fetch content updates from multiple RSS feeds, and publish them in Twitter and Telegram.

# How to use Sputnik V2?
SputnikV2 can be made functional through simple steps.

Install the requirements.

```
pip3 install -r requirements.txt
```

## Setting up author-Twitter handle database and linking it
Currently the feature is implemented using Google sheets. Refer pygsheets documentation for more information.

## Setting up Twitter/Telegram credentials
Apply for a developer account at https://dev.twitter.com/. Fill up the credentials in 'twitterConf.py'. Similaryly get the Telegram credentials filled in 'teleConf.py' for posting in Telegram channel.


## Running the code
Sputnik V2 is made to run on its own until it is interrupted. To run it in the foreground invoke the Python interpreter as follows, from the folder containing the code.

```
python main.py
```

If you want it to run the Python script in the background, issue the following in the terminal.

```
nohup python main.py &
```

Follow me at https://www.twitter.com/pratheesh