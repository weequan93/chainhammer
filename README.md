```
NEWS 2019-Feb-23 - video!
Explaining software v55 video released on youtube:
```
--> [watch](https://www.youtube.com/watch?v=xTYnsfs5U7I)

![chainhammer-logo.png](docs/chainhammer-logo.png)

---

# chainhammer v59
TPS measurements of parity aura, geth clique, quorum, tobalaba, etc. 
It should work with any Ethereum type chain; we focused on PoA consensus.

## instructions

### video
The brand new release v55 is now presented & explained in a useful [video on youtube](https://www.youtube.com/watch?v=xTYnsfs5U7I).

### folders
* `hammer/` - submits many transactions, while watching the recent blocks
* `reader/` - reads blocks; visualizes TPS, blocktime, gas, bytes - see [reader/README.md](reader/README.md)
* `docs/` - see esp. reproduce.md, cloud.md, FAQ.md, **new:** azure.md
* `results/` - for each client one markdown file; `results/runs/` - auto-generated pages
* `logs/` - check this first if problems
* `networks/` - network starters & external repos via install script, see below
* `scripts/` - installers and other iseful bash scripts
* `env/` - Python virtualenv, created via install script, see below
* `tests/` - start whole integration test suite via `./pytest.sh`

### chronology
See the [results/](results/) folder:

1. [log.md](results/log.md): initial steps; also tried *Quorum's private transactions*
1. [quorum.md](results/quorum.md): raft consensus, quorum is a geth fork
1. [tobalaba.md](results/tobalaba.md): parity fork of  EnergyWebFoundation
1. [quorum-IBFT.md](results/quorum-IBFT.md): IstanbulBFT, 2nd consensus algo in quorum
1. [geth.md](results/geth.md): geth clique PoA algorithm
1. [parity.md](results/parity.md): parity aura PoA algorithm, many attempts to accelerate
1. [eos.md](results/eos.md): not begun yet
1. [substrate.md](results/substrate.md): not begun yet

## results summary

**Outdated table** in which I had run each of the experiments *manually* 
in autumn 2018; *soon* re-done completely, using the below automation. 
So please contact me *now*, if you know how to accelerate any of these clients:

| hardware  	| node type 	    | #nodes 	| config 	| peak TPS_av 	| final TPS_av 	|
|-----------	|-----------	    |--------	|--------	|-------------	|--------------	|
| t2.micro 	    | parity aura   	| 4      	| (D)    	| 45.5        	|  44.3        |
| t2.large 	    | parity aura   	| 4      	| (D)    	| 53.5        	|  52.9        |
| t2.xlarge 	| parity aura   	| 4      	| (J)    	| 57.1        	|  56.4        |
| t2.2xlarge 	| parity aura   	| 4      	| (D)    	| 57.6        	|  57.6        |
|               |                   |           |        	|         	    |              |
| t2.micro 	    | parity instantseal | 1      	| (G)    	| 42.3        	|  42.3        |
| t2.xlarge	    | parity instantseal | 1      	| (J)    	| 48.1        	|  48.1        |
|               |                   |           |        	|         	    |              |
| t2.2xlarge 	| geth clique     	| 3+1 +2    | (B)    	| 421.6       	| 400.0        |
| t2.xlarge 	| geth clique     	| 3+1 +2    | (B)    	| 386.1       	| 321.5        |
| t2.xlarge 	| geth clique     	| 3+1       | (K)    	| 372.6       	| 325.3        |
| t2.large 	    | geth clique     	| 3+1 +2    | (B)    	| 170.7       	| 169.4        |
| t2.small 	    | geth clique     	| 3+1 +2    | (B)    	|  96.8       	|  96.5        |
| t2.micro 	    | geth clique     	| 3+1       | (H)    	| 124.3       	| 122.4        |
|               |                   |           |        	|         	    |              |
| t2.micro SWAP | quorum crux IBFT 	| 4    	    | (I) SWAP! |  98.1         |  98.1   	   |
|               |                   |           |        	|         	    |              |
| t2.micro 	    | quorum crux IBFT 	| 4    	    | (F)     	| lack of RAM   |         	   |
| t2.large 	    | quorum crux IBFT 	| 4    	    | (F)    	| 207.7      	| 199.9        |
| t2.xlarge 	| quorum crux IBFT 	| 4    	    | (F)    	| 439.5      	| 395.7        |
| t2.xlarge 	| quorum crux IBFT 	| 4    	    | (L)    	| 389.1      	| 338.9        |
| t2.2xlarge 	| quorum crux IBFT 	| 4    	    | (F)    	| 435.4      	| 423.1        |
| c5.4xlarge 	| quorum crux IBFT 	| 4    	    | (F)  test_getNearestEntry()  	| 536.4      	| 524.3        |

[Reproduce](docs/reproduce.md) these results easily; for the `config` column also see there.
Quickest reproduction with my [Amazon AMI readymade image](docs/reproduce.md#readymade-amazon-ami).
And see that bottom of [parity.md](results/parity.md) and [geth.md](results/geth.md) 
and [quorum-IBFT.md](results/quorum-IBFT.md) for the latest runs, issues, and additional details.

## faster wider more
* how I initially got this faster, *on Quorum*, step by step, please do read the 1st logbook [log.md](results/log.md)
* then I improved per client, see each in [#chronology](#chronology) above
* (possible [TODOs](docs/TODO.md) - any other ideas?)

but not much more needed = the current version is already fully automated. Use it! May it help you to improve the speed of your Ethereum client!

### you
Add yourself to [other-projects.md](docs/other-projects.md) using chainhammer, or projects which are similar to this.   

(Especially if you work in one of the dev teams, you know your client code best - ) please try to improve the above results, e.g. by varying the CLI arguments with which the nodes are started; I don't see that as my job, you will be much more successful with that.

See parity [PE#9393](https://github.com/paritytech/parity-ethereum/issues/9393), parity [SE#58521](https://ethereum.stackexchange.com/questions/58521/parity-tps-optimization-please-help), geth [GE#17447](https://github.com/ethereum/go-ethereum/issues/17447), quorum [Q#479](https://github.com/jpmorganchase/quorum/issues/479#issuecomment-413603316).

*Please report back when you have done other / new measurements.*


## install and run
All this is developed and much tested on Debian, locally and in the AWS cloud. New: Ubuntu now also supported, see below.

### quickstart
N.B.: Better do this on a *disposable cloud, or virtualbox machine*; because the installation makes lasting changes and needs sudo!  

After unpacking a ZIP of the downloaded repo, or by
```
git clone https://github.com/drandreaskrueger/chainhammer drandreaskrueger_chainhammer
ln -s drandreaskrueger_chainhammer CH
cd CH
```

you now only need these **two lines** *to prepare and run the 1st experiment!*
```
scripts/install.sh
CH_TXS= 5000  CH_THREADING="sequential" ./run.sh $HOSTNAME-TestRPC testrpc
```
You will then have a diagram, and a HTML and MD page about this run!

(on **Ubuntu** instead: `scripts/install.sh docker ubuntu` )

#### activate docker 

Better now *logout & login*, or *close the terminal, and open a new terminal*, because the above scripts/install.sh might have enabled docker for the the first time for this user. Then:

#### All supported clients in one go:

For the **full integration test**, run each client for a short moment:
```
export CH_MACHINE=yourChoice
./run-all_small.sh
```

For detailed instructions, please see [docs/](docs/), esp. [reproduce.md](docs/reproduce.md), and for troubleshooting [FAQ.md](docs/FAQ.md) and [github issues](https://github.com/drandreaskrueger/chainhammer/issues).

## benchmarking a remote node
Chainhammer can now be stripped down to its pure benchmarking abilities, i.e. without the installation of docker and without the three local network starters (parity-deploy, geth-dev, quorum-crux). It was successfully used to benchmark the Microsoft Azure blockchain-as-a-service product.  The essential difference is to start the installation with the switch `nodocker`:

    scripts/install.sh nodocker

So, if you just want to benchmark your *existing Ethereum node or network*, have a look at the manual [docs/azure.md](docs/azure.md) . 

## unittests
```
./pytest.sh
```
enables the virtualenv, 
then starts a `testrpc-py` Ethereum simulator on http://localhost:8545 in the background, 
logging into `tests/logs/`; 
then runs `./deploy.py andtests`; 
and finally runs all the unittests, also logging into `tests/logs/`.  

(Instead of testrpc-py) if you want to run tests with another node, 
just start that; and run `pytest` manually:
```
source env/bin/activate
py.test -v --cov
```

There were 98 tests on January 23rd, all 98 PASSED
(see this [logfile](tests/logs/tests-with_testrpc-py.log.ansi)  --> 
`cat tests/logs/*.ansi` because colors) on these different Ethereum providers:  

* testrpc instantseal (`testrpc-py`)  13 seconds 
* geth Clique (`geth-dev`) 63 seconds
* quorum IBFT (`blk-io/crux`) 59 seconds
* parity instantseal (`parity-deploy`) 8 seconds
* parity aura (`parity-deploy`) 72 seconds

## credits

Please credit this as:

> benchmarking scripts "chainhammer"  
> maintainer: Dr Andreas Krueger 2018-2020  
> https://github.com/drandreaskrueger/chainhammer   

Consider to submit your improvements & [usage](docs/other-projects.md) as pull request. Thanks.

### development was supported by

> v01-v35 financed by Electron.org.uk 2018  
> v40-v55 financed by Web3Foundation 2018-2019  
> v58-v59 financed by Microsoft Azure 2019  

![logo](img/web3_foundation_grants_badge_black_smaller.png)

Thank you very much!

### short summary

> The open source tools 'chainhammer' submits a high load of 
> smart contract transactions to an Ethereum based blockchain, 
> then 'chainreader' reads the whole chain, and 
> produces diagrams of TPS, blocktime, gasUsed and gasLimit, and the blocksize.
> https://github.com/drandreaskrueger/chainhammer    

---

---

---

```
# The following diagrams are outdated! Just make your own, new ones, with:
CH_MACHINE=yourChoice ./run-all_large.sh
```

## chainhammer: hammer --> reader -->  diagrams
examples:

### geth clique on AWS t2.xlarge 
[geth.md](results/geth.md) = geth (go ethereum client), "Clique" consensus.

50,000 transactions to an Amazon t2.xlarge machine.

Interesting artifact that after ~14k transactions, the speed drops considerably - but recovers again. [Reported](https://github.com/ethereum/go-ethereum/issues/17447#issuecomment-431629285).

![geth-clique-50kTx_t2xlarge_tps-bt-bs-gas_blks12-98.png](reader/img/geth-clique-50kTx_t2xlarge_tps-bt-bs-gas_blks12-98.png)  
reader/img/geth-clique-50kTx_t2xlarge_tps-bt-bs-gas_blks12-98.png

### quorum IBFT on AWS t2.xlarge 

[quorum-IBFT.md](results/quorum-IBFT.md) = Quorum (geth fork), IBFT consensus, 20 millions gasLimit, 1 second istanbul.blockperiod; 20000 transactions multi-threaded with 23 workers. Initial average >400 TPS then drops to below 300 TPS, see [quorum issue](https://github.com/jpmorganchase/quorum/issues/479#issuecomment-413603316))

![quorum-crux-IBFT_t2xlarge_tps-bt-bs-gas_blks320-395.png](reader/img/quorum-crux-IBFT_t2xlarge_tps-bt-bs-gas_blks320-395.png)


### quorum raft
OLD RUN on a desktop machine.  

[quorum.md](results/quorum.md) = Quorum (geth fork), raft consensus,  5000  transactions multi-threaded with 23 workers, average TPS around 160 TPS, and 20 raft blocks per second)
![reader/img/quorum_tps-bt-bs-gas_blks242-357.png](reader/img/quorum_tps-bt-bs-gas_blks242-357.png)


### tobalaba
OLD RUN on a desktop machine.

[tobalaba.md](results/tobalaba.md) = Public "Tobalaba" chain of the EnergyWebFoundation (parity fork), PoA; 20k transactions; > 150 TPS if client is well-connected.

![reader/img/tobalaba_tps-bt-bs-gas_blks5173630-5173671.png](reader/img/tobalaba_tps-bt-bs-gas_blks5173630-5173671.png)

### parity aura v1.11.11 on AWS t2.xlarge 
[parity.md#run-18](results/parity.md#run-18) = 
using [parity-deploy.sh](https://github.com/paritytech/parity-deploy) 
dockerized network of 4 local nodes with increased gasLimit, and 5 seconds blocktime; 
20k transactions; ~ 60 TPS on an Amazon t2.xlarge machine.

N.B.: Could not work with parity v2 yet because of bugs 
[PD#76](https://github.com/paritytech/parity-deploy/issues/76) and 
[PE#9582](https://github.com/paritytech/parity-ethereum/issues/9582) --> 
everything still on parity v1.11.11

![parity-v1.11.11-aura_t2xlarge_tps-bt-bs-gas_blks5-85.png](reader/img/parity-v1.11.11-aura_t2xlarge_tps-bt-bs-gas_blks5-85.png)  
parity-v1.11.11-aura_t2xlarge_tps-bt-bs-gas_blks5-85.png


**Calling all parity experts: How to improve these too slow TPS results?**
    
See issue [PE#9393](https://github.com/paritytech/parity-ethereum/issues/9393), 
and the [detailed log of what I've tried already](results/parity.md), 
and the 2 shortest routes to reproducing the results: [reproduce.md](docs/reproduce.md).    

Thanks.

./send_multi_transfer_chain.py  100  threaded2 10  2

./send_multi_transfer_erc20.py  100  threaded2 10  2

## 

./tps.py &
./deploy.py &
./send_multi_high_gas.py  5000  threaded2 100 0 > "../logs/send_multi_high_gas.py.log" &
./send_multi_high_gas.py  5000  threaded2 100  1 > "../logs/send_multi_high_gas.py.1.log" &
./send_multi_high_gas.py  5000  threaded2 100  2 > "../logs/send_multi_high_gas.py.2.log" &
./send_multi_high_gas.py  5000  threaded2 100  3 > "../logs/send_multi_high_gas.py.3.log" &
./send_multi_high_gas.py  5000  threaded2 100  4 > "../logs/send_multi_high_gas.py.4.log" &
./send_multi_high_gas.py  5000  threaded2 100  5 > "../logs/send_multi_high_gas.py.5.log" &
./send_multi_high_gas.py  5000  threaded2 100  6 > "../logs/send_multi_high_gas.py.6.log" &
./send_multi_high_gas.py  5000  threaded2 100  7 > "../logs/send_multi_high_gas.py.7.log" &
./send_multi_high_gas.py  5000  threaded2 100  8 > "../logs/send_multi_high_gas.py.8.log" &
./send_multi_high_gas.py  5000  threaded2 100  9 > "../logs/send_multi_high_gas.py.9.log" &
./send_multi_high_gas.py  5000  threaded2 100  10 > "../logs/send_multi_high_gas.py.10.log" &
./send_multi_high_gas.py  5000  threaded2 100  11 > "../logs/send_multi_high_gas.py.11.log" &
./send_multi_high_gas.py  5000  threaded2 100  12 > "../logs/send_multi_high_gas.py.12.log" &
./send_multi_high_gas.py  5000  threaded2 100  13 > "../logs/send_multi_high_gas.py.13.log" &
./send_multi_high_gas.py  5000  threaded2 100  14 > "../logs/send_multi_high_gas.py.14.log" &
./send_multi_high_gas.py  5000  threaded2 100  15 > "../logs/send_multi_high_gas.py.15.log" &
./send_multi_high_gas.py  5000  threaded2 100  16 > "../logs/send_multi_high_gas.py.16.log" &
./send_multi_high_gas.py  5000  threaded2 100  17 > "../logs/send_multi_high_gas.py.17.log" &
./send_multi_high_gas.py  5000  threaded2 100  18 > "../logs/send_multi_high_gas.py.18.log" &
./send_multi_high_gas.py  5000  threaded2 100  19 > "../logs/send_multi_high_gas.py.19.log" &
./send_multi_high_gas.py  5000  threaded2 100  20 > "../logs/send_multi_high_gas.py.20.log" &
./send_multi_high_gas.py  5000  threaded2 100  21 > "../logs/send_multi_high_gas.py.21.log" &
./send_multi_high_gas.py  5000  threaded2 100  22 > "../logs/send_multi_high_gas.py.22.log" &
./send_multi_high_gas.py  5000  threaded2 100  23 > "../logs/send_multi_high_gas.py.23.log" &
./send_multi_high_gas.py  5000  threaded2 100  24 > "../logs/send_multi_high_gas.py.24.log" &
./send_multi_high_gas.py  5000  threaded2 100  25 > "../logs/send_multi_high_gas.py.25.log" &
./send_multi_high_gas.py  5000  threaded2 100  26 > "../logs/send_multi_high_gas.py.26.log" &
./send_multi_high_gas.py  5000  threaded2 100  27 > "../logs/send_multi_high_gas.py.27.log" &
./send_multi_high_gas.py  5000  threaded2 100  28 > "../logs/send_multi_high_gas.py.28.log" &
./send_multi_high_gas.py  5000  threaded2 100  29 > "../logs/send_multi_high_gas.py.29.log" &
./send_multi_high_gas.py  5000  threaded2 100  30 > "../logs/send_multi_high_gas.py.30.log" &
./send_multi_high_gas.py  5000  threaded2 100  31 > "../logs/send_multi_high_gas.py.31.log" &
./send_multi_high_gas.py  5000  threaded2 100  32 > "../logs/send_multi_high_gas.py.32.log" &
./send_multi_high_gas.py  5000  threaded2 100  33 > "../logs/send_multi_high_gas.py.33.log" &
./send_multi_high_gas.py  5000  threaded2 100  34 > "../logs/send_multi_high_gas.py.34.log" &
./send_multi_high_gas.py  5000  threaded2 100  35 > "../logs/send_multi_high_gas.py.35.log" &
./send_multi_high_gas.py  5000  threaded2 100  36 > "../logs/send_multi_high_gas.py.36.log" &
./send_multi_high_gas.py  5000  threaded2 100  37 > "../logs/send_multi_high_gas.py.37.log" &
./send_multi_high_gas.py  5000  threaded2 100  38 > "../logs/send_multi_high_gas.py.38.log" &
./send_multi_high_gas.py  5000  threaded2 100  39 > "../logs/send_multi_high_gas.py.39.log" &
./send_multi_high_gas.py  5000  threaded2 100  40 > "../logs/send_multi_high_gas.py.40.log" &
./send_multi_high_gas.py  5000  threaded2 100  41 > "../logs/send_multi_high_gas.py.41.log" &
./send_multi_high_gas.py  5000  threaded2 100  42 > "../logs/send_multi_high_gas.py.42.log" &
./send_multi_high_gas.py  5000  threaded2 100  43 > "../logs/send_multi_high_gas.py.43.log" &
./send_multi_high_gas.py  5000  threaded2 100  44 > "../logs/send_multi_high_gas.py.44.log" &
./send_multi_high_gas.py  5000  threaded2 100  45 > "../logs/send_multi_high_gas.py.45.log" &
./send_multi_high_gas.py  5000  threaded2 100  46 > "../logs/send_multi_high_gas.py.46.log" &
./send_multi_high_gas.py  5000  threaded2 100  47 > "../logs/send_multi_high_gas.py.47.log" &
./send_multi_high_gas.py  5000  threaded2 100  48 > "../logs/send_multi_high_gas.py.48.log" &
./send_multi_high_gas.py  5000  threaded2 100  49 > "../logs/send_multi_high_gas.py.49.log" &
./send_multi_high_gas.py  5000  threaded2 100  50 > "../logs/send_multi_high_gas.py.50.log" &
./send_multi_high_gas.py  5000  threaded2 50  51 > "../logs/send_multi_high_gas.py.51.log" &
./send_multi_high_gas.py  5000  threaded2 50  52 > "../logs/send_multi_high_gas.py.52.log" &
./send_multi_high_gas.py  5000  threaded2 50  53 > "../logs/send_multi_high_gas.py.53.log" &
./send_multi_high_gas.py  5000  threaded2 50  54 > "../logs/send_multi_high_gas.py.54.log" &
./send_multi_high_gas.py  5000  threaded2 50  55 > "../logs/send_multi_high_gas.py.55.log" &
./send_multi_high_gas.py  5000  threaded2 50  56 > "../logs/send_multi_high_gas.py.56.log" &
./send_multi_high_gas.py  5000  threaded2 50  57 > "../logs/send_multi_high_gas.py.57.log" &
./send_multi_high_gas.py  5000  threaded2 50  58 > "../logs/send_multi_high_gas.py.58.log" &
./send_multi_high_gas.py  5000  threaded2 50  59 > "../logs/send_multi_high_gas.py.59.log" &


./send_multi_transfer_erc20.py  5000  threaded2 50  0 > "../logs/send_multi_transfer_erc20.py.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  1 > "../logs/send_multi_transfer_erc20.py.1.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  2 > "../logs/send_multi_transfer_erc20.py.2.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  3 > "../logs/send_multi_transfer_erc20.py.3.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  4 > "../logs/send_multi_transfer_erc20.py.4.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  5 > "../logs/send_multi_transfer_erc20.py.5.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  6 > "../logs/send_multi_transfer_erc20.py.6.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  7 > "../logs/send_multi_transfer_erc20.py.7.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  8 > "../logs/send_multi_transfer_erc20.py.8.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  9 > "../logs/send_multi_transfer_erc20.py.9.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  10 > "../logs/send_multi_transfer_erc20.py.10.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  11 > "../logs/send_multi_transfer_erc20.py.11.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  12 > "../logs/send_multi_transfer_erc20.py.12.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  13 > "../logs/send_multi_transfer_erc20.py.13.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  14 > "../logs/send_multi_transfer_erc20.py.14.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  15 > "../logs/send_multi_transfer_erc20.py.15.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  16 > "../logs/send_multi_transfer_erc20.py.16.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  17 > "../logs/send_multi_transfer_erc20.py.17.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  18 > "../logs/send_multi_transfer_erc20.py.18.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  19 > "../logs/send_multi_transfer_erc20.py.19.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  20 > "../logs/send_multi_transfer_erc20.py.20.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  21 > "../logs/send_multi_transfer_erc20.py.21.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  22 > "../logs/send_multi_transfer_erc20.py.22.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  23 > "../logs/send_multi_transfer_erc20.py.23.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  24 > "../logs/send_multi_transfer_erc20.py.24.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  25 > "../logs/send_multi_transfer_erc20.py.25.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  26 > "../logs/send_multi_transfer_erc20.py.26.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  27 > "../logs/send_multi_transfer_erc20.py.27.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  28 > "../logs/send_multi_transfer_erc20.py.28.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  29 > "../logs/send_multi_transfer_erc20.py.29.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  30 > "../logs/send_multi_transfer_erc20.py.30.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  31 > "../logs/send_multi_transfer_erc20.py.31.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  32 > "../logs/send_multi_transfer_erc20.py.32.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  33 > "../logs/send_multi_transfer_erc20.py.33.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  34 > "../logs/send_multi_transfer_erc20.py.34.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  35 > "../logs/send_multi_transfer_erc20.py.35.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  36 > "../logs/send_multi_transfer_erc20.py.36.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  37 > "../logs/send_multi_transfer_erc20.py.37.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  38 > "../logs/send_multi_transfer_erc20.py.38.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  39 > "../logs/send_multi_transfer_erc20.py.39.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  40 > "../logs/send_multi_transfer_erc20.py.40.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  41 > "../logs/send_multi_transfer_erc20.py.41.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  42 > "../logs/send_multi_transfer_erc20.py.42.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  43 > "../logs/send_multi_transfer_erc20.py.43.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  44 > "../logs/send_multi_transfer_erc20.py.44.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  45 > "../logs/send_multi_transfer_erc20.py.45.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  46 > "../logs/send_multi_transfer_erc20.py.46.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  47 > "../logs/send_multi_transfer_erc20.py.47.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  48 > "../logs/send_multi_transfer_erc20.py.48.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  49 > "../logs/send_multi_transfer_erc20.py.49.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  50 > "../logs/send_multi_transfer_erc20.py.50.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  51 > "../logs/send_multi_transfer_erc20.py.51.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  52 > "../logs/send_multi_transfer_erc20.py.52.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  53 > "../logs/send_multi_transfer_erc20.py.53.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  54 > "../logs/send_multi_transfer_erc20.py.54.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  55 > "../logs/send_multi_transfer_erc20.py.55.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  56 > "../logs/send_multi_transfer_erc20.py.56.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  57 > "../logs/send_multi_transfer_erc20.py.57.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  58 > "../logs/send_multi_transfer_erc20.py.58.log" &
./send_multi_transfer_erc20.py  5000  threaded2 50  59 > "../logs/send_multi_transfer_erc20.py.59.log" &



./send_multi_transfer_chain.py  5000  threaded2 50  0 > "../logs/send_multi_transfer_chain.py.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  1 > "../logs/send_multi_transfer_chain.py.1.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  2 > "../logs/send_multi_transfer_chain.py.2.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  3 > "../logs/send_multi_transfer_chain.py.3.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  4 > "../logs/send_multi_transfer_chain.py.4.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  5 > "../logs/send_multi_transfer_chain.py.5.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  6 > "../logs/send_multi_transfer_chain.py.6.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  7 > "../logs/send_multi_transfer_chain.py.7.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  8 > "../logs/send_multi_transfer_chain.py.8.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  9 > "../logs/send_multi_transfer_chain.py.9.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  10 > "../logs/send_multi_transfer_chain.py.10.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  11 > "../logs/send_multi_transfer_chain.py.11.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  12 > "../logs/send_multi_transfer_chain.py.12.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  13 > "../logs/send_multi_transfer_chain.py.13.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  14 > "../logs/send_multi_transfer_chain.py.14.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  15 > "../logs/send_multi_transfer_chain.py.15.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  16 > "../logs/send_multi_transfer_chain.py.16.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  17 > "../logs/send_multi_transfer_chain.py.17.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  18 > "../logs/send_multi_transfer_chain.py.18.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  19 > "../logs/send_multi_transfer_chain.py.19.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  20 > "../logs/send_multi_transfer_chain.py.20.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  21 > "../logs/send_multi_transfer_chain.py.21.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  22 > "../logs/send_multi_transfer_chain.py.22.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  23 > "../logs/send_multi_transfer_chain.py.23.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  24 > "../logs/send_multi_transfer_chain.py.24.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  25 > "../logs/send_multi_transfer_chain.py.25.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  26 > "../logs/send_multi_transfer_chain.py.26.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  27 > "../logs/send_multi_transfer_chain.py.27.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  28 > "../logs/send_multi_transfer_chain.py.28.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  29 > "../logs/send_multi_transfer_chain.py.29.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  30 > "../logs/send_multi_transfer_chain.py.30.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  31 > "../logs/send_multi_transfer_chain.py.31.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  32 > "../logs/send_multi_transfer_chain.py.32.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  33 > "../logs/send_multi_transfer_chain.py.33.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  34 > "../logs/send_multi_transfer_chain.py.34.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  35 > "../logs/send_multi_transfer_chain.py.35.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  36 > "../logs/send_multi_transfer_chain.py.36.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  37 > "../logs/send_multi_transfer_chain.py.37.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  38 > "../logs/send_multi_transfer_chain.py.38.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  39 > "../logs/send_multi_transfer_chain.py.39.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  40 > "../logs/send_multi_transfer_chain.py.40.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  41 > "../logs/send_multi_transfer_chain.py.41.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  42 > "../logs/send_multi_transfer_chain.py.42.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  43 > "../logs/send_multi_transfer_chain.py.43.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  44 > "../logs/send_multi_transfer_chain.py.44.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  45 > "../logs/send_multi_transfer_chain.py.45.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  46 > "../logs/send_multi_transfer_chain.py.46.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  47 > "../logs/send_multi_transfer_chain.py.47.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  48 > "../logs/send_multi_transfer_chain.py.48.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  49 > "../logs/send_multi_transfer_chain.py.49.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  50 > "../logs/send_multi_transfer_chain.py.50.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  51 > "../logs/send_multi_transfer_chain.py.51.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  52 > "../logs/send_multi_transfer_chain.py.52.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  53 > "../logs/send_multi_transfer_chain.py.53.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  54 > "../logs/send_multi_transfer_chain.py.54.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  55 > "../logs/send_multi_transfer_chain.py.55.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  56 > "../logs/send_multi_transfer_chain.py.56.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  57 > "../logs/send_multi_transfer_chain.py.57.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  58 > "../logs/send_multi_transfer_chain.py.58.log" &
./send_multi_transfer_chain.py  5000  threaded2 50  59 > "../logs/send_multi_transfer_chain.py.59.log" &



// 

docker build . --tag quanquanah/chainhammer:mac
docker buildx build --platform linux/amd64 . --tag quanquanah/chainhammer:linux


RPC=http
PRIVATE_KEY_ADDRESS=0x
PRIVATE_KEY=0x
KEY_PER_WORKER=200
GAS_LIMIT=3500000



0xe9aDfB912642A75068a297849eC0D040C0B1d0BF

docker run --rm -it -e RPC="https://rpc.deriw.com" -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" -e KEY_PER_WORKER=200 -e GAS_LIMIT=3500000 quanquanah/chainhammer:mac
CONTRACT_ADDRESS=0x29C70BA9672498C2DF296e5FeD89564CbED2df5f
//erc20 0x35b3ac4003e1AfeE7601C190DB4f039fCb1BbcB5


 docker run --rm -it \
  --entrypoint python \
  -e RPC="https://rpc.deriw.com" \
  -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" \
  -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" \
  -e KEY_PER_WORKER=200 \
  -e GAS_LIMIT=3500000 \
  quanquanah/chainhammer:mac \
  ./deploy.py


 docker run --rm -it \
  --entrypoint python \
  -e RPC="http://172.16.35.43:8449" \
  -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" \
  -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" \
  -e KEY_PER_WORKER=200 \
  -e GAS_LIMIT=3500000 \
  quanquanah/chainhammer:linux \
  ./tps.py





for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
  docker run --rm -d \
    --name chainhammer$i \
    --entrypoint python \
    -e RPC="http://172.16.35.43:8449" \
    -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" \
    -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" \
    -e KEY_PER_WORKER=400 \
    -e GAS_LIMIT=1100000 \
    -e CONTRACT_ADDRESS=0x29C70BA9672498C2DF296e5FeD89564CbED2df5f \
    -v "$(pwd)/../logs:/app/logs" \
    quanquanah/chainhammer:linux \
    ./send_multi_high_gas.py 5000 threaded2 100 $i
done


for i in 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40; do
  docker run --rm -d \
    --name chainhammer$i \
    --entrypoint python \
    -e RPC="http://172.16.35.43:8449" \
    -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" \
    -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" \
    -e KEY_PER_WORKER=400 \
    -e GAS_LIMIT=1100000 \
    -e CONTRACT_ADDRESS=0x29C70BA9672498C2DF296e5FeD89564CbED2df5f \
    -v "$(pwd)/../logs:/app/logs" \
    quanquanah/chainhammer:linux \
    ./send_multi_high_gas.py 5000 threaded2 100 $i
done

for i in 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60; do
  docker run --rm -d \
    --name chainhammer$i \
    --entrypoint python \
    -e RPC="http://172.16.35.43:8449" \
    -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" \
    -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" \
    -e KEY_PER_WORKER=400 \
    -e GAS_LIMIT=1100000 \
    -e CONTRACT_ADDRESS=0x29C70BA9672498C2DF296e5FeD89564CbED2df5f \
    -v "$(pwd)/../logs:/app/logs" \
    quanquanah/chainhammer:linux \
    ./send_multi_high_gas.py 5000 threaded2 100 $i
done









for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
  docker run --rm -d \
    --name chainhammer$i \
    --entrypoint python \
    -e RPC="http://172.16.35.43:8449" \
    -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" \
    -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" \
    -e KEY_PER_WORKER=400 \
    -e GAS_LIMIT=1100000 \
    -e CONTRACT_ADDRESS=0xe9aDfB912642A75068a297849eC0D040C0B1d0BF \
    -v "$(pwd)/../logs:/app/logs" \
    quanquanah/chainhammer:linux \
    ./send_multi_transfer_erc20.py 5000 threaded2 200 $i
done

for i in 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40; do
  docker run --rm -d \
    --name chainhammer$i \
    --entrypoint python \
    -e RPC="http://172.16.35.43:8449" \
    -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" \
    -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" \
    -e KEY_PER_WORKER=400 \
    -e GAS_LIMIT=1100000 \
    -e CONTRACT_ADDRESS=0xe9aDfB912642A75068a297849eC0D040C0B1d0BF \
    -v "$(pwd)/../logs:/app/logs" \
    quanquanah/chainhammer:linux \
    ./send_multi_transfer_erc20.py 5000 threaded2 200 $i
done


for i in 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60; do
  docker run --rm -d \
    --name chainhammer$i \
    --entrypoint python \
    -e RPC="http://172.16.35.43:8449" \
    -e PRIVATE_KEY_ADDRESS="0x94A6713cbF5F589aB51570D0b4cd219792421af2" \
    -e PRIVATE_KEY="0x3f924b934c41a048183b48835acdb533b1d07045a38394b006b238a3fc07ea89" \
    -e KEY_PER_WORKER=400 \
    -e GAS_LIMIT=1100000 \
    -e CONTRACT_ADDRESS=0xe9aDfB912642A75068a297849eC0D040C0B1d0BF \
    -v "$(pwd)/../logs:/app/logs" \
    quanquanah/chainhammer:linux \
    ./send_multi_transfer_erc20.py 5000 threaded2 200 $i
done




