import requests
import json
import os
cookies = {
    'PREF': 'hl=en&tz=UTC',
    'SOCS': 'CAI',
    'GPS': '1',
    'YSC': 'ypCO9qGoKSY',
    'VISITOR_INFO1_LIVE': 'qBJvehrqV6s',
    'VISITOR_PRIVACY_METADATA': 'CgJJThIEGgAgKA%3D%3D',
}
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us,en;q=0.5',
    'Sec-Fetch-Mode': 'navigate',
    'X-Youtube-Client-Name': '5',
    'X-Youtube-Client-Version': '19.09.3',
    'Origin': 'https://www.youtube.com',
}
params = {
    'key': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
    'prettyPrint': 'false',
}
json_data = {
    'context': {
        'client': {
            'clientName': 'IOS',
            'clientVersion': '19.09.3',
            'deviceModel': 'iPhone14,3',
            'userAgent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
            'hl': 'en',
            'timeZone': 'UTC',
            'utcOffsetMinutes': 0,
        },
    },
    'videoId': 'k5yYu12zZYI',
    'playbackContext': {
        'contentPlaybackContext': {
            'html5Preference': 'HTML5_PREF_WANTS',
        },
    },
    'contentCheckOk': True,
    'racyCheckOk': True,
}
response = requests.post(
    'https://www.youtube.com/youtubei/v1/player',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
#pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]


pr = response.json()['streamingData']["adaptiveFormats"]

l = []
for __ in pr:
    if "1080p" in str(__) and "mp4" in str(__):
        l.append(__)
    if "AUDIO_QUALITY_MEDIUM" in str(__) and not 'isDrc' in str(__):
        l.append(__)


#print(l)
v = l[0]['url']
##print(v)
a = l[-1]['url']
#print(a)

#os.system(f"ffmpeg -re -i '{v}' -re -i '{a}' -filter_complex \"[0:v]scale=256/81*iw:256/81*ih,boxblur=luma_radius=min(h\,w)/40:luma_power=3:chroma_radius=min(cw\,ch)/40:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,setsar=1,crop=w=iw*81/256\" -acodec copy -preset ultrafast -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js")


#os.system(f"ffmpeg -re -i '{pr}' -map 0:p:5 -filter_complex \"[0:v]scale=256/81*iw:256/81*ih,boxblur=luma_radius=min(h\,w)/40:luma_power=3:chroma_radius=min(cw\,ch)/40:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,setsar=1,crop=w=iw*81/256\" -acodec copy -preset ultrafast -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js")


os.system(f"ffmpeg -re -i '{v}' -re -i '{a}' -filter_complex '[0:v]scale=ih*16/9:-1,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,crop=h=iw*9/16' -acodec copy -preset ultrafast -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js")


#print(f"ffmpeg -re -i '{pr}' -map 0:p:2 -filter_complex \"[0:0]split[main][back];[back]scale=1280:720[scale];[scale]drawbox=x=0:y=0:w=1280:h=720:color=black:t=1000[draw];[main]scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)'[proc];[draw][proc]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2\" -c:a aac -g 20 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/mrak-pqgz-91hz-9r9u-2twa")

#print(pr)
#os.system(f"ffmpeg -re -ss 05:58:48 -i \"{pr}\" -map 0:p:13 -vf transpose=1 -c:v libx264 -b:v 8000k -c:a aac -g 30 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/mrak-pqgz-91hz-9r9u-2twa")


#os.system(f"ffmpeg -re -i \"{pr}\" -map 0:p:2 -vf scale=ih*4/3:ih,setsar=1 -c:a aac -g 30 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/mrak-pqgz-91hz-9r9u-2twa")


#ffmpeg -i input.mp4 -vf "crop=in_w:in_h*(9/16), pad=in_w:in_h*(16/9):(ow-iw)/2:(oh-ih)/2" output.mp4
 # dhdjdidu
# -----
