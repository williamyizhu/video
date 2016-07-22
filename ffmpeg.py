play_list = ['Last Week in Dance']

import os
import subprocess
import shutil

os.environ['PATH'] = os.environ['PATH'] + ':' + '/usr/local/bin'

vid_ext = 'mp4'
sub_lang = 'zh-Hans'
sub_ext = 'vtt'
sub_fontsize = '24'

movie_root_dir = '/Users/williamyizhu/Movies/'
movie_with_subs_dir = movie_root_dir + '_video_upload/'

def vidprocess(ptitle):
    vpath = movie_root_dir + ptitle
    os.chdir(vpath)
    vsfile = os.listdir(vpath)    
    
    vpath2 = movie_with_subs_dir + ptitle
    if not os.path.exists(vpath2):
        os.makedirs(vpath2)
    
#     vfile is a list of all video files
    vfile = [s for s in vsfile if ".mp4" in s]
    
    for video in vfile:
        subs = '.'.join([video[:-4], sub_lang, sub_ext])
#         print subs
        vpath3 = vpath2 + '/' + video
        if subs in vsfile:
            print subs
            subprocess.call(['ffmpeg', '-y', '-i', subs, 'temp.ass'])
            subprocess.call(['ffmpeg', '-y', '-i', video, '-vf', 'subtitles=temp.ass:force_style=\'FontSize='+sub_fontsize+'\'', vpath3])
        else:
            print video + ' has no subtitle file'
            shutil.move(video, vpath3)


for pp in play_list:        
    vidprocess(pp)

