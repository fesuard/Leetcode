// https://leetcode.com/problems/is-object-empty/description
// Given an object or an array, return if it is empty.
// An empty object contains no key-value pairs.
// An empty array contains no elements.
// You may assume the object or array is the output of JSON.parse.


// We first check if the obj is an array, then return it's length == 0,
// if it's not an array we return the length of the object keys == 0.
const isEmpty = function(obj) {
    
    if(Array.isArray(obj)){
        return obj.length === 0;
    }
    else{
        return Object.keys(obj).length === 0;
    }
};
