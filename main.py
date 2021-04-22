import requests
import re

source = requests.get(input('Please enter playlist link: ')).text


id_index_list = [m.start() for m in re.finditer('watch\\?v\\=', source)] #regular expression (regex)


anon_playlist_id_long = 'https://www.youtube.com/watch_videos?video_ids='
for i in id_index_list:
    anon_playlist_id_long += source[i+8:i+ 19] + ','
 

#anon_playlist_id_source = requests.get(anon_playlist_id[:-1])
list_id = requests.get(anon_playlist_id_long[:-1]).url
list_id = list_id[44:]
playlist_url_final = 'https://www.youtube.com/playlist?' + list_id
print('Here is the link to your anonymous playlist: \n\n\n' + playlist_url_final)
input('\n\n\npress any key to exit')