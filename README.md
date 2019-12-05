# deep-chip
Texas Holdem bot

[Project definition](https://github.com/RealLankinen/deep-chip/blob/master/documentation/project-definition.md)


## Weekly updates
[1. week](https://github.com/RealLankinen/deep-chip/blob/master/documentation/weekly-progress-1.md) | [2. week](https://github.com/RealLankinen/deep-chip/blob/master/documentation/weekly-progress-2.md) | [3. week](https://github.com/RealLankinen/deep-chip/blob/master/documentation/weekly-progress-3.md) | [4. week](https://github.com/RealLankinen/deep-chip/blob/master/documentation/weekly-progress-4.md) | [5. week](https://github.com/RealLankinen/deep-chip/blob/master/documentation/weekly-progress-5.md)

## Installation
```
git clone https://github.com/RealLankinen/deep-chip.git
```
In this project I needed to modify PyPokerEngine which this is using a lot and that is why you also need to install it differently than normally.
```
pip install git+https://github.com/RealLankinen/PyPokerEngine.git
```

## Usage
Go to the root folder of this project and run: 
```bash
python -m src.main
```

## Tests
Go to the root folder of this project and run: 
```bash
python -m unittest
```


## Test coverage
Name                                                                         Stmts Miss  Cover

src/__init__.py                                                                0      0   100%

src/algorithms.py                                                             64     41    36%

src/main.py                                                                    7      0   100%

src/player.py                                                                 37     11    70%

src/state_handler.py                                                         139    124    11%

TOTAL                                                                       1705    781    54%

