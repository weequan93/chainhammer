// simplestorage contract
// chainhammer v46

pragma solidity ^0.4.21;

contract simplestorage {
    uint256 public storedData;
    uint256 public num;

    // a=70000  gas =  50,000,000
    // a=20000 gas = 20000
    // a=50000  gas =  30,000,000
    // a=10000  gas =  gas=6,000,000
    // a=1500 gas=1,000,000
    // a=3300  gas=2,000,000
    // a =5000, gas=3,000,000
    uint256 public a = 70000;

    function set() external {
        // try failing transactions:
        // assert ( 1 == 0 );  // uses up all 90000 given gas
        // revert();           // uses 41686 gas
        // throw;              // same as revert();
        // require ( 1 == 0 ); // uses 41714 gas

        for (uint256 i = 0; i < a; i++) {
            num += a;
        }
    }

    function get() view returns (uint256 retVal) {
        return storedData;
    }
}
