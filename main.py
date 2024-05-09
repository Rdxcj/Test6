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
    'videoId': 'rGlJhoE2vME',
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
pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]
#os.system(f"ffmpeg -re -i '{pr}' -map 0:p:2 -filter_complex \"[0:v]scale=256/81*iw:256/81*ih,boxblur=luma_radius=min(h\,w)/40:luma_power=3:chroma_radius=min(cw\,ch)/40:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,setsar=1,crop=w=iw*81/256\" -c:a aac -g 20 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/fkhh-v2kz-fpgj-be4h-8fv2")
#os.system(f"ffmpeg -re -i '{pr}' -map 0:p:2 -filter_complex \"[0:0]split[main][back];[back]scale=1920:1080[scale];[scale]drawbox=x=0:y=0:w=1920:h=1080:color=black:t=1000[draw];[main]scale='if(gt(a,16/9),1920,-1)':'if(gt(a,16/9),-1,1080)'[proc];[draw][proc]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2\" -c:a aac -g 20 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/z7mc-58xj-mzvc-mqyp-86vj")


#print(f"ffmpeg -re -i '{pr}' -map 0:p:2 -filter_complex \"[0:0]split[main][back];[back]scale=1280:720[scale];[scale]drawbox=x=0:y=0:w=1280:h=720:color=black:t=1000[draw];[main]scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)'[proc];[draw][proc]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2\" -c:a aac -g 20 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/mrak-pqgz-91hz-9r9u-2twa")


#os.system(f"ffmpeg -re -i \"{pr}\" -map 0:p:2 -vf \"transpose=1\" -c:a aac -g 20 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/mrak-pqgz-91hz-9r9u-2twa")


os.system(f"ffmpeg -re -i \"{pr}\" -map 0:p:2 -vf scale=1280:-2 -c:a aac -g 20 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/mrak-pqgz-91hz-9r9u-2twa")


#ffmpeg -i input.mp4 -vf "crop=in_w:in_h*(9/16), pad=in_w:in_h*(16/9):(ow-iw)/2:(oh-ih)/2" output.mp4
