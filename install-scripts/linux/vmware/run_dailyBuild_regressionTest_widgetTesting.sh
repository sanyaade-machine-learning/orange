DISPLAY=george:1
export DISPLAY
cd /home/vmware
L=( winXP.dailyBuild winXP.regressionTests winXP.widgetTesting )

for f in "${L[@]}"; do
	echo "running VM $f" 
	# copy original VM image into a temporary location
	rm -Rf cron.$f
	cp -R /vmware/orangeBuildTest.VMWAREimage/$f cron.$f

	# run it
	echo "\"cron.$f/Windows\ XP\ Professional.vmx\"" > runThis.lst
	# kill after 1 hour
	ulimit -t 7200
	echo "started at"
	date
	/usr/local/bin/vmware -geometry 1200x1000+0+0 -x -q -k runThis.lst
	echo done
	date
	echo

	# remove temp VM image
	rm -Rf cron.$f
done

