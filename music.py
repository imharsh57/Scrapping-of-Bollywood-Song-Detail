
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:17:11 2019

@author: Harsh Anand
"""


from bs4 import BeautifulSoup 
import requests  
import re    
song = []
movie = []
singers = []
musicians = []
lyricists = []
year = []
lyrics = []
i=1
while(i<42):
    url = "https://www.lyricsbell.com/hindi-songs/page/"+str(i)+"/"
    i+=1

 
    source = requests.get(url).text
    soup = BeautifulSoup(source,"lxml")
    
    
    #collect links in single page for songs
    album_link = []
    
    get_result = soup.find('div',class_='site-content')
    for row in get_result.find_all('h2',class_='entry-title'):
        for link in row.find_all('a', href=True):
            album_link.append(link['href'])
    

    
    
    #song,movie,singer,.....
    for item in album_link:
        #print(item)
        song_c=0
        movie_c=0
        singer_c=0
        music_c=0
        lyrics_c=0
        date_c=0
        temp = requests.get(item).text
        #print(temp)
        temp_soup = BeautifulSoup(temp,"lxml")
        
        
        
        #find year
        for date in temp_soup.find_all('span',class_='postDate'):
            #print(date.text)
            temp_date = date.text.split(", ")
            temp_date = temp_date[1]
            year.append(temp_date)
            date_c=1
            
        
        #song,movie,singer,.....
        temp_get_result = temp_soup.find('div',class_='lyrics-detail')
        #print(temp_get_result)
        temp_get_result = temp_get_result.find('p')
        temp_get_result = temp_get_result.text.split('\n')
        
        for k in range(0,len(temp_get_result)):
            #result_temp = temp_get_result[k].split(' – ')
            result_temp = re.split(' – |: ',temp_get_result[k])
            
            # print(result_temp[1])
            if result_temp[0] == 'Song':
                song.append(result_temp[1])
                song_c=1
            
                
            elif re.findall(r'Movie',result_temp[0]):
                movie.append(result_temp[1])
                movie_c=1
            
                
            elif re.findall(r'Singers',result_temp[0]):
                singers.append(result_temp[1])
                singer_c=1
            
            
                
            elif re.findall(r'Musicians',result_temp[0]):
                musicians.append(result_temp[1])
                music_c=1
            
                
            elif re.findall(r'Lyricist',result_temp[0]):
                lyricists.append(result_temp[1])
                lyrics_c=1
                

        if song_c==0:
            song.append("-")
        if movie_c==0:
            movie.append("-")
        if singer_c==0:
            singers.append("-")
        if music_c==0:
            musicians.append("-")
        if lyrics_c==0:
            lyricists.append("-")
        if date_c==0:
            year.append(" ")
            
            
        
   
            
            
        
        
        #lyrics
        temp_get_lyrics = temp_soup.find_all('div',class_='lyrics-col')
        temp_get_lyrics = temp_get_lyrics[1]
        
        temp_lyrics = []
    
        for p in temp_get_lyrics.find_all('p'):
            #print(p.text)
            p=p.text.split("\n")
            p = ' '.join(p)
            temp_lyrics.append(p)
            
        temp_lyrics = ' '.join(temp_lyrics)
        
        lyrics.append(temp_lyrics)
        
import pandas as pd
from collections import OrderedDict

col_name = ["Song","Movie","Singers","Musicians","Lyricists","Year","Lyrics"]
col_data = OrderedDict(zip(col_name,[song,movie,singers,musicians,lyricists,year,lyrics]))
df = pd.DataFrame(col_data) 


#df.to_csv("page1-29songs1.csv")
'''
import pandas as pd
df1 = pd.read_csv("page1-29songs1.csv")
df2 = pd.read_csv("page1-29songsp-43.csv")
df3 = pd.read_csv("page1-29songsp-46-51.csv")
df4 = pd.read_csv("page1-29songsp-53-61.csv")
df5 = pd.read_csv("page1-29songsp-62-64.csv")
frames = [df1, df2, df3,df4,df5]
result = pd.concat(frames)

result = result.drop('Unnamed: 0',axis=1)
result = result.drop('Year',axis=1)

result = result.reset_index()
result = result.drop('index',axis=1)

result.to_csv("song-hindi.csv")
'''

'''      page 46-51 & page 53-61 & page 62-65
############################### page 43 ####################################################################
from bs4 import BeautifulSoup 
import requests  
import re    
song = []
movie = []
singers = []
musicians = []
lyricists = []
year = []
lyrics = []
i=43
while(i<44):
    url = "https://www.lyricsbell.com/hindi-songs/page/"+str(i)+"/"
    i+=1

 
    source = requests.get(url).text
    soup = BeautifulSoup(source,"lxml")
    
    
    #collect links in single page for songs
    album_link = []
    
    get_result = soup.find('div',class_='site-content')
    for row in get_result.find_all('h2',class_='entry-title'):
        for link in row.find_all('a', href=True):
            album_link.append(link['href'])
    

    
    
    #song,movie,singer,.....
    for item in album_link:
        #print(item)
        song_c=0
        movie_c=0
        singer_c=0
        music_c=0
        lyrics_c=0
        date_c=0
        temp = requests.get(item).text
        #print(temp)
        temp_soup = BeautifulSoup(temp,"lxml")
        
        
        
        #find year
        for date in temp_soup.find_all('span',class_='postDate'):
            #print(date.text)
            temp_date = date.text.split(", ")
            temp_date = temp_date[1]
            year.append(temp_date)
            date_c=1
            
        #song,movie,singer,.....
        temp_get_result = temp_soup.find('div',class_="width:100%;position:relative")
        temp_get_result=temp_get_result.findNext('div',{'class':"lyrics-col"}).findNext('div',{'class':"lyrics-detail"}).findNext('p').findNext('p').findNext('p')
#####################################################################
# page 46-51 & page 53-61 & page 62-65
# temp_get_result=temp_get_result.findNext('div',{'class':"lyrics-col"}).findNext('div',{'class':"lyrics-detail"}).findNext('div',{'class':"lyrics-col"}).findNext('div',{'class':"lyrics-detail"}).findNext('p').findNext('p').findNext('p')
##########################################################################
        #print(temp_get_result)
        
        temp_get_result = temp_get_result.text.split('\n')
        
        for k in range(0,len(temp_get_result)):
            #result_temp = temp_get_result[k].split(' – ')
            result_temp = re.split(' – |: ',temp_get_result[k])
            
            # print(result_temp[1])
            if result_temp[0] == 'Song':
                song.append(result_temp[1])
                song_c=1
            
                
            elif re.findall(r'Movie',result_temp[0]):
                movie.append(result_temp[1])
                movie_c=1
            
                
            elif re.findall(r'Singers',result_temp[0]):
                singers.append(result_temp[1])
                singer_c=1
            
            
                
            elif re.findall(r'Musicians',result_temp[0]):
                musicians.append(result_temp[1])
                music_c=1
            
                
            elif re.findall(r'Lyricist',result_temp[0]):
                lyricists.append(result_temp[1])
                lyrics_c=1
                

        if song_c==0:
            song.append("-")
        if movie_c==0:
            movie.append("-")
        if singer_c==0:
            singers.append("-")
        if music_c==0:
            musicians.append("-")
        if lyrics_c==0:
            lyricists.append("-")
        if date_c==0:
            year.append(" ")
         
            
        
        
        #lyrics
        temp_get_lyrics = temp_soup.find_all('div',class_='lyrics-col')
        temp_get_lyrics = temp_get_lyrics[1]
        
        temp_lyrics = []
    
        for p in temp_get_lyrics.find_all('p'):
            #print(p.text)
            p=p.text.split("\n")
            p = ' '.join(p)
            temp_lyrics.append(p)
            
        temp_lyrics = ' '.join(temp_lyrics)
        
        lyrics.append(temp_lyrics)
        
import pandas as pd
from collections import OrderedDict

col_name = ["Song","Movie","Singers","Musicians","Lyricists","Year","Lyrics"]
col_data = OrderedDict(zip(col_name,[song,movie,singers,musicians,lyricists,year,lyrics]))
df = pd.DataFrame(col_data) 


#df.to_csv("page1-29songsp-43.csv")

''' #*********************************************************************************************



