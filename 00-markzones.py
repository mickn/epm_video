from glob import glob
import os,shapely,sys
from video_analysis import viz_vidtools

import sys

def set_zones(who='*',sec=70):
    print("Press 'q' then ENTER in zone-setting window to skip to next video")
    print("Close zone-setting window to return to ipython prompt") 
    wait = raw_input("PRESS ENTER TO START SETTING ZONES")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    vids = [f for f in glob(dir_path+'/'+who+'.mp4') if not os.path.exists(viz_vidtools.epm_cfg_fn(f))]
    print vids
    vids = sorted(vids)
    for i,vid in enumerate(vids):
        print >> sys.stderr, 'Video %s of %s' % (i+1, len(vids))
        print >> sys.stderr, ''
        try:
            viz_vidtools.get_epm_config(vid=vid,sec=sec) # Seconds for keyframe to set zones
        except IOError:
            continue
        except ValueError:
            continue
set_zones() # Or set_zones('x'), where x can be *F2*, *F1*, *xf*, etc.   

print "Now, we'll set the points"

from glob import glob
import os
from video_analysis import viz_vidtools
vidsNoPointsSetYet = [f for f in glob('*.mp4') if not os.path.exists(viz_vidtools.epm_cfg_fn(f))]
vidsOfInterest = [768]
vids = [x for x in vidsNoPointsSetYet for y in vidsOfInterest if '_'+str(y)+'_' in x]
for vid in vids:
    viz_vidtools.get_epm_config(vid,70)