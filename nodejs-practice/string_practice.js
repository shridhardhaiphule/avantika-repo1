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

function jumbleWord(word) {
    return word
        .split('')
        .sort(() => Math.random() - 0.5)
        .join('');
}

let words = "practice"
console.log("Original word:", words);
console.log("Jumbled word:", jumbleWord(words));
