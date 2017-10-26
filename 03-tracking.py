from glob import glob
from py_util import SLURM,run_safe
import os

vids_timeframe = glob('*_EPM_*/*.timeframe.tuple') 

# Every round decrease the duration of tracking by 5 seconds because some videos have cv2 errors and only solution I've found is to track until before the error happens

for seconds in [0,5,10,15,20,25,30]:

    not_tracked = [os.path.dirname(v)+'.mp4' for v in vids_timeframe if not glob(os.path.dirname(v)+'/*timepoint_cv2.done')]
    trd = {}

    queue = 'serial_requeue' #SLURM
    for nt in not_tracked:
        timeframe = eval(open(os.path.join(nt[:-4],os.path.basename(nt[:-4]+'.timeframe.tuple'))).read())
        finished_base = nt[:-4]+'/timepoint_cv2'
        if timeframe[0] < 6:
            start = 6
        else: 
            start = timeframe[0]
        if timeframe[1]:
            end = timeframe[1]
            if end - start > 313:
                end = timeframe[0] + 313
        else:
            end = timeframe[0] + 313
        # Uncomment the line below if videos fail tracking to track fewer seconds and reduce by more seconds each round
        end = end - seconds
        cmd = 'summarize_segment_opencv2.py -s %s -e %s -mt 0.25 -tr invert -oe shapely -l 200 %s' % (start, end, nt) #no video output
        #cmd = 'summarize_segment_opencv2.py -s %s -e %s -mt 0.25 -tr invert -oe shapely -vs timepoint_good -l 200 %s' % (start, end, nt)
        print cmd
        try:
            run_safe.add_cmd(trd,finished_base,cmd,force_write=True)
        except:
            continue

    logfile = 'log/EPM_20170719_113000_%s_seconds_less' % seconds

    try:
        SLURM.run_until_done(trd,'tracked',logfile,120,8192,200,queue,MAX_RETRY=0)
    except IOError:
        continue