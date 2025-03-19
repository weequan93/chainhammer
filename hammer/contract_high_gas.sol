// simplestorage contract
// chainhammer v46

pragma solidity ^0.4.21;

contract simplestorage {
    uint256 public storedData;
    uint256 public num;

    // 1m gas 25000
    // 2m gas 25000
    // 3m gas 25000
    uint256 public a = 25000;

    function set(uint256 x) {
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
