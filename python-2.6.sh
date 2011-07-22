#!/bin/bash

. /broad/tools/scripts/useuse
reuse .cellprofiler-0.10.1
export PYTHONPATH=$PYTHONPATH:/imaging/analysis/People/imageweb/batchprofiler/cgi-bin/CellProfiler2.0/python/lib/Python2.6/site-packages
export MPLCONFIGDIR=/imaging/analysis/CPCluster/CellProfiler-2.0/.matplotlib
export LAST_CHECKOUT=`echo "import os;cpdir='/imaging/analysis/CPCluster/CellProfiler-2.0';print os.path.join(cpdir,str(max(*[int(x) for x in os.listdir(cpdir) if x.isdigit()])))" | python`
if [ -n "$CELLPROFILER_USE_XVFB" ]
then
#
# Set up X -> Xvfb
#
DISPLAY=:$LSB_JOBID
echo "Xvfb display = $DISPLAY"
tmp=/local/scratch/CellProfilerXVFB.$RANDOM.$RANDOM
echo "Xvfb directory = $tmp"
mkdir $tmp
Xvfb $DISPLAY -fbdir $tmp &
XVFBPID=$!
echo "Xvfb PID = $XVFBPID"
python "$@"
kill $XVFBPID
sleep 5
rmdir $tmp
else
python "$@"
fi
