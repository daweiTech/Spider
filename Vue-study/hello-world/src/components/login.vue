<template>
    <div class="container search-container">
      <h1 class="title">baidu-search</h1>
      <input type="text" class="form-control" placeholder="请输入想要搜索关键字" v-model="keyword" @keyup="get($event)"
             @keydown.down.prevent="selectDown"
             @keydown.up.prevent="selectUp">
      <ul>
        <li class="text-left" v-for="(value,index) in myData"><span class="text-success textprimary"
                                                                      :class="{gray:index==now}">{{value}}</span></li>
      </ul>
      <p>
      <h2 v-show="myData.length==0" class="text-warning text-left">(*^__^*)暂时没有数据</h2>
      </p>
    </div>
  </template>
  <script>
    export default {
      data() {
        return {
          myData:[],
          keyword:'',
          now:-1
        }
      },
      methods:{
        get:function (event) {
          if(event.keyCode==38||event.keyCode==40)return;
          if(event.keyCode==13){
            window.open('https://www.baidu.com/s?wd='+this.keyword);
            this.keyword=''
          }
          this.$http.jsonp('https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?', {
            params: {
              wd: this.keyword
            },
            jsonp: 'cb'
          }).then((res) => {
            console.log("res11",res)
            this.myData = res.body.s
          })
        },
        selectDown:function () {
          this.now++;
          if(this.now==this.myData.length)this.now=-1;
          console.log(this.now)
          this.keyword=this.myData[this.now];
        },
        selectUp:function () {
          this.now--;
          if(this.now==-2)this.now=this.myData.length-1;
          this.keyword=this.myData[this.now];
        }
      }
    }
  </script>
  
  <style scoped>
    /*body {*/
    /*  background-image: url("../../assets/background.jpg");*/
    /*  background-size: cover;*/
    /*}*/
  
    .title {
      color: #ffffff;
      text-align: left;
    }
  
    .gray {
      background-color: #dff0d8;
    }
  
    .textprimary {
      color: #3c763d;
      text-align: left;
      font-family: "Microsoft YaHei UI";
      font-size: larger;
      font-weight: bolder;
      font-size: 16px;
    }
    ul {
      list-style: none;
      top: 0px;
      left: -40px;
      right: 0px;
      position:relative;
    }
    ul :hover {
      cursor: pointer;
      background-color:#EEEEEE
    }
    li {
      list-style: none;
      top: 0px;
      left: 0px;
      right: 0px;
    }
  </style>