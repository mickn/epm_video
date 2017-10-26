from glob import glob
import os
from video_analysis import viz_vidtools
vidsNoPointsSetYet = [f for f in glob('*.mp4') if not os.path.exists(viz_vidtools.epm_cfg_fn(f))]
print vidsNoPointsSetYet
vidsOfInterest = [768, 769, 771, 772, 796, 797, 813, 814, 815, 826, 827, 839, 842, 843, 844, 845, 847, 857, 858, 861, 862, 863, 1181, 1183, 1184, 1191, 1193, 1333, 1442, 1454, 1506, 2075, 2080, 2112, 2114, 2115, 2121, 2177, 2193, 2194, 2197, 2202, 2268, 2270, 2285, 2313]
vids = [x for x in vidsNoPointsSetYet for y in vidsOfInterest if '_'+str(y)+'_' in x]
for vid in vids:
    print vid
    viz_vidtools.get_epm_config(vid, 7)