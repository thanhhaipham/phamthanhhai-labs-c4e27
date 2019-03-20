from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs'
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode('utf-8')

soup = BeautifulSoup(html_content,'html.parser')
section = soup.find('section','section chart-grid')

li_list = section.div.ul.find_all('li')
song_list=[]
song_lst=[]
for li in li_list:
    h3 = li.h3.a
    h4 = li.h4.a
    song = h3.string
    artist = h4.string
    news = OrderedDict({
    'song': song.lstrip().rstrip(),
    'artist': artist
    })
    song_list.append(news)
    song_lst.append(song)


pyexcel.save_as(records = song_list,dest_file_name='songlist.xlsx')

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 5, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(song_lst)