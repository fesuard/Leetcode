// https://leetcode.com/problems/create-hello-world-function/description
// Write a function createHelloWorld. It should return a new function that always returns "Hello World".


const createHelloWorld = function() {
    const greeting = "Hello World";

    return function(...args) {
        return greeting;
    }
};
