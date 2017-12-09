# Project info
The included set of programs:
1. Gather information on modern kanji use by scraping tweets from Japanese Twitter accounts
2. Collect kanji used in Japanese Language Proficiency Test (JLPT) and in Japanese school curriculum (Jōyō)
3. Show what percentage of kanji of variying difficulty is used by some Japanese Twitter account

# Requirements
Python 3<br/>
Flask<br/>
Chrome<br/>

# Getting started
1. Fork/download repo
2. Enter the downloaded directory
3. If I did not give you a copy of auth_info.txt:<br/>
&nbsp;a. Create auth_info.txt using your favorite editor<br/>
&nbsp;b. Go to https://apps.twitter.com/ and create a new app<br/>
&nbsp;c. Click on your app<br/>
&nbsp;d. Locate your auth info in the 'Keys and Access Tokens' tab<br/>
&nbsp;e. Fill out the fields in auth_info.txt as shown in auth_info_template.txt

# (Optional) Collecting tweets
Some sample .xml files have been provided in this repo. But, they can be generated again if desired.<br/>

To collect recent tweets from a particular user:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;run `python3 get_tweets.py @SomeUsername`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this creates a @SomeUsername.xml file in the xml folder<br/>
To collect recent tweets from a set of predefined users<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;run `python3 get_tweets.py`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this creates a tweets.xml file in the xml/ folder<br/>

# (Optional) Extracting kanji
The necessary .txt files have been provided in this repo. But, they can be generated again if desired.<br/>

To extract only the kanji from the provided .csv files containing JLPT/Jōyō kanji guides:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;run `python3 get_kanji.py`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this creates several .txt files in the kanji/txt/ folder<br/>

# Comparing kanji use and displaying the results
1. run `python3 project.py`<br/>
2. Open http://127.0.0.1:5000/ in Chrome
3. Enter a username for which an .xml file has been generated. The following work given the provided files:<br/>
&nbsp;&nbsp;@hajimesyacho<br/>
&nbsp;&nbsp;@ariyoshihiroiki<br/>
&nbsp;&nbsp;@matsu_bouzu<br/>
&nbsp;&nbsp;@pamyurin<br/>
&nbsp;&nbsp;@nhk_news<br/>
&nbsp;&nbsp;@kojiharunyan<br/>
&nbsp;&nbsp;@itoi_shigesato<br/>
&nbsp;&nbsp;@sugitaLOV<br/>
4. Quit the terminal program at any time via Ctrl-C
