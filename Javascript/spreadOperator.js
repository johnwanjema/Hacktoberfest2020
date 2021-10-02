Allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected, 
or an object expression to be expanded in places where zero or more key-value pairs (for object literals) are expected.

//sum the arguments of a function
function sum(x, y, z) {
  return x + y + z;
}

const numbers = [1, 2, 3];

console.log(sum(...numbers));


//Spread operator conact two arrays
let arr = [1,2,3];
let arr2 = [4,5,6];

arr = [...arr,...arr2];
console.log(arr); // [ 1, 2, 3, 4, 5, 6 ]

//Spread operator copy an array
let arr = ['A','B','C'];
let arr2 = [...arr
console.log(arr2); // [ 'A', 'B', 'C', 'D' ]

//Spread operator copy an array
let arr = ['a','b'];
let arr2 = [arr,'c','d'];
console.log(arr2); // [ [ 'a', 'b' ], 'c', 'd' ]


//Join two objects
const user1 = {
    name: 'John',
    age: 12,
};
  
const user2 = {
    name: "Doe",
    location: "Nairobi" 
};
  
const mergedUsers = {...user1, ...user2};
console.log(mergedUsers)

