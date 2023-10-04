console.log('123123')
// D:\nodejs\node.exe E:\图灵Python学习\爬虫\JS语法学习\01-demo.js

// 单行注释
/*
* 多行注释
*
*
* */
var pi = 3.14
//const = 3.14
console.log(pi)//console打印输出
console.log(typeof pi)//number

var name = "David"
console.log(name,pi)

//大小写敏感
var Xialuo = 1
var xialuo = 2
console.log(Xialuo,xialuo)

//先创建再赋值，改值
var x
console.log(x)//输出undefined

x = 1
console.log(x)

x = 2
console.log(x)

// let a = 1
// console.log(a)
// let a = 2
// console.log(a)//报错

//一般写JS逆向，用var
person = new Object();
person.firstname = "John"
console.log(person)

car = ['梅赛德斯','特斯拉']
console.log(car[0])
car1 = {name:'特斯拉',age:'18'}
console.log(car1.name)
console.log(car1['age'])


var persons = {
    firstName: "xl",
    lastName : "lili",
    id : 5566,
    fullName : function()
	{
       return this.firstName + " " + this.lastName;
    }
};
console.log(persons.fullName())


function test(){
    console.log("这是测试函数test")
}
test()

nba = function (a,b,c){
    console.log(b)
}
nba('tom','kevin')