# defaults:
DBFILE=temp.db
INFOFILE=hammer/last-experiment.json
TPSLOG=logs/tps.py.log
DEPLOYLOG=logs/deploy.py.log

SENDLOG=logs/send_multi.py.log
SENDLOG1=logs/send_multi.1.py.log
SENDLOG2=logs/send_multi.2.py.log
SENDLOG3=logs/send_multi.3.py.log
SENDLOG4=logs/send_multi.4.py.log
SENDLOG5=logs/send_multi.5.py.log
SENDLOG6=logs/send_multi.6.py.log
SENDLOG7=logs/send_multi.7.py.log
SENDLOG8=logs/send_multi.8.py.log
SENDLOG9=logs/send_multi.9.py.log
SENDLOG10=logs/send_multi.10.py.log

if [ -z "$CH_TXS" ] || [ -z "$CH_THREADING" ]; then 
    echo "You must set 2 ENV variables, examples:"
    echo "export CH_TXS=1000 CH_THREADING=sequential"
    echo "export CH_TXS=5000 CH_THREADING=\"threaded2 20\""
    exit
fi

INFOWORD=$1

# exit when any command fails
set -e
# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo; echo "\"${last_command}\" command filed with exit code $?."' EXIT
#

function title {
    echo =============================
    echo = $1
    echo ============================= 
}  

echo 

title "chainhammer v52 - run all ="
echo
echo infoword: $INFOWORD
echo number of transactions: $CH_TXS 
echo concurrency algo: $CH_THREADING
echo
echo infofile: $INFOFILE
echo blocks database: $DBFILE
echo log files:
echo $TPSLOG
echo $DEPLOYLOG
echo $SENDLOG
echo

# exit



title "activate virtualenv" 
source myenv/bin/activate
echo
python --version
echo 

cd hammer
rm -f $INFOFILE



title tps.py
echo start listener tps.py, show here but also log into file $TPSLOG
echo this ENDS after send.py below writes a new INFOFILE $INFOFILE
./tps.py | tee "../$TPSLOG" &
TPS_PID=$!
echo

title sleep 1.5 seconds
echo to have tps.py say its thing before deploy.py starts printing
echo
sleep 1.5
echo 

title deploy.py
echo Deploy the smartContract, deploy.py will then trigger tps.py to START counting. 
echo Logging into file $DEPLOYLOG.
echo 
./deploy.py > "../$DEPLOYLOG"
sleep 0
echo

title send.py
echo Send $CH_TXS transactions with non/concurrency algo \'$CH_THREADING\', plus possibly wait 10 more blocks.
echo Then send.py triggers tps.py to end counting. Logging all into file $SENDLOG. 
echo

echo 0
./send_multi.py $CH_TXS $CH_THREADING 0 > "../$SENDLOG" &

echo 1
./send_multi.py $CH_TXS $CH_THREADING 1 > "../$SENDLOG1" &

echo 2
./send_multi.py $CH_TXS $CH_THREADING 2 > "../$SENDLOG2" &

echo 3
./send_multi.py $CH_TXS $CH_THREADING 3 > "../$SENDLOG3" &

echo 4
./send_multi.py $CH_TXS $CH_THREADING 4 > "../$SENDLOG4" &

echo 5
./send_multi.py $CH_TXS $CH_THREADING 5 > "../$SENDLOG5" &

echo 6
./send_multi.py $CH_TXS $CH_THREADING 6 > "../$SENDLOG6" &

echo 7
./send_multi.py $CH_TXS $CH_THREADING 7 > "../$SENDLOG7" &

# echo 8
# ./send_multi.py $CH_TXS $CH_THREADING 8 > "../$SENDLOG8" &

# echo 9
# ./send_multi.py $CH_TXS $CH_THREADING 9 > "../$SENDLOG9" &


echo

title "sleep 2"
echo wait 2 second until also tps.py has written its results.
echo
sleep 2
echo



cd ..


wait $BACK_PID
title "Ready."

echo


