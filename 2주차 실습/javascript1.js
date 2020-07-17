// 0. 기타
// 이 줄 주석 처리
console.log('hello!'); // 여기도 주석

/* 
안녕하세요 피로그래밍 여러분!
이 부분은 주석 처리되고 있습니다.
*/

//1. 변수 선언
var j;
const x = 123;
let y = 3;

// error!
// x = 321;

// no error
y = 10;

// 2. 조건문

let a = 2;
let b = 1;
let c = 3;

a === b; // 같음
a !== b; // 다름
a === b && a === c; // &&: and
a === b || a !== c; // ||: or
a > b; // 대소관계

if (a > b) {
  console.log('a is more than b.');
} else if (a == b) {
  console.log('a is the same as b.');
} else {
  document.write('a is less than b.');
}

//3. 함수
function sayHello() {
  console.log('hello');
}

sayHello();

const adder = (a, b) => {
  return a + b;
};

a = 1;
b = 2;
console.log(adder(a, b));

//4.array
let job = [];

// 없는 인덱스 넘버로 접근해서 바로 값 할당 가능
job[0] = 'Warrior';
job[1] = 'Archer';
job[2] = 'Wizard';

console.log(job);

// 곧바로 선언 가능
let numbers = [1, 2, 3];
console.log(numbers);

//5.object
let player1 = {};

// object의 key 와 value를 python과 같이 할당 가능
player1.hp = 100;
player1.mp = 300;

let player2 = {
  hp: 200,
  mp: 200,
};

console.log(player1);
console.log(player2);

//6. 조건문
for (let k = 0; k < 5; k++) {
  console.log(k);
}
console.log('--------');
let r = 0;
while (r < 5) {
  console.log(r);
  r++;
}

const arr = [10, 20, 30, 40, 50];

for (const i of arr) {
  console.log(i);
}

let arra = [10, 20, 30, 40, 50];

arra.forEach(value => {
  console.log(value);
});
console.log('--------');
arra.map(value => {
  console.log(value);
});
console.log('--------');
arra.map((index, value) => {
  console.log(index);
  console.log(value);
});

//7. 삼항연산자
//D = A ? B : C
//A가 true면 B가, false이면 C가 D에 할당된다.
const z = 2;
for (let x = 1; x <= 5; x++) {
  console.log(x === z ? 'correct' : 'incorrect');
}
