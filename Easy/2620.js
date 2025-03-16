// https://leetcode.com/problems/counter/description
// Given an integer n, return a counter function. This counter function initially returns n and then 
// returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).


// In a closure, the inner function has access to the variables defined in the outer function, so after
// we create counter1 = createCounter(n), each time we call counter 1, it will increment by n++
const createCounter = function(n) {

    return function() {
        return n++;
    };
};
