from glob import glob
import os,shapely,sys
from video_analysis import viz_vidtools

import sys

def set_zones(who='*',sec=70):
    print("Press 'q' then ENTER in zone-setting window to skip to next video")
    print("Close zone-setting window to return to ipython prompt") 
    wait = raw_input("PRESS ENTER TO START SETTING ZONES")
    vids = [f for f in glob(who+'.mp4') if not os.path.exists(viz_vidtools.epm_cfg_fn(f))]
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
set_zones('20170530_113304_EPM_PO_11597_M',70) # Or set_zones('x'), where x can be *F2*, *F1*, *xf*, etc.   