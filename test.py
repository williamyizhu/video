import pandas

import matplotlib

import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)
dx, dy = np.meshgrid(points, points)
z = (np.sin(dx)+np.sin(dy))
plt.imshow(z)
plt.colorbar()
plt.title('plot for sin(x)+sin(y)')
plt.show()

#===============================================================================
# testing code
#===============================================================================
# indexes = [i for i, x in enumerate(vfile) if '.mp4' in x]
# matching = [s for s in vfile if ".mp4" in s]    
    
# subprocess.call(['ffmpeg', '-y', '-i', video, '-vf', 'subtitles=temp.ass', vpath2+video])
    
# mg = 'ffmpeg -y -i 2-20160418-0HQYh8x7VKk.mp4 -vf subtitles=2-20160418-0HQYh8x7VKk.zh-Hans.vtt oo.mp4'
# subprocess.call(mg.split())
#                  
# # return an error if there is no subtitle stream embedded in a mp4 file
# subprocess.call(["ffmpeg", "-i", "Subtitles-sub.mp4", "-vf", "subtitles=Subtitles-sub.mp4", "out-sub.mp4"])
# subprocess.Popen(["ffmpeg", "-i", "Subtitles.mp4", "-vf", "subtitles=Subtitles.mp4", "out.mp4"])
# 
# # call youtube-dl
# mk = 'youtube-dl --write-auto-sub --sub-lang zh-Hans https://www.youtube.com/watch?v=bVCvthr95io'
# subprocess.call(mk.split())
# 
# mk = 'youtube-dl --write-auto-sub --sub-lang zh-Hans https://www.youtube.com/playlist?list=PL0jyq5z3EBnlkic18Q3z9IHk9bjj6ziOR'
# subprocess.call(mk.split())
# 
# subprocess.call(["ls","-l"])
# subprocess.call(["ffmpeg","-h"])
# subprocess.call(["youtube-dl","-h"])


