function jumbleWord(word) {
    return word.split('').sort(() => Math.random() - 0.5).join('');
}

let str = "Hello";
console.log("Original String:", str);

console.log("Uppercase:", str.toUpperCase());
console.log("Lowercase:", str.toLowerCase());

let dateStr = "2025-09-23";
let dateObj = new Date(dateStr);
console.log("Date object:", dateObj);
console.log("Year:", dateObj.getFullYear());
console.log("Month:", dateObj.getMonth() + 1);
console.log("Day:", dateObj.getDate());

let fruits = "apple,banana,cherry";
let arr = fruits.split(",");
console.log("Split array:", arr);

let word = "practice";
console.log("Original Word:", word);
console.log("Jumbled Word:", jumbleWord(word));