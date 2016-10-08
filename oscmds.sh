#!/bin/sh
cd photos
echo "Taking the Photo"
now=$1 #Now is the filename time stamp
#take pic
fswebcam -d /dev/video0 $now.jpg
echo "Pic Taken"
echo""
#ring Bell
echo "Ringing Bell"
echo ""
echo ""
cd ..
omxplayer DBSE.mp3
