
# Convert rss feeds to audio

Create an audio file of news summaries from different rss feeds. Inspired from https://github.com/KPGunner/news_feed/

---

Can use directly in another python program or through CLI.

**Python**

```python
from rss_to_audio import create_audio

feeds = ['http://www.wsj.com/xml/rss/3_7085.xml','http://www.wsj.com/xml/rss/3_7455.xml']
file_name = 'wsj.mp3'
create_audio(feeds,file_name)
```
**CLI**

*args:*

- *feeds* = location of a text file that has a rss feed url on each line
- *filename* = name of final audio file


```
echo "http://www.wsj.com/xml/rss/3_7085.xml" > feeds.txt
python rss_to_audio.py feeds.txt news.mp3
```
