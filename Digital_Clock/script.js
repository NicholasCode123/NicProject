let h=document.querySelector(".h");
let m=document.querySelector(".m");
let s=document.querySelector(".s");
setInterval(()=>{
  let timeNow=new Date();
h.innerHTML=timeNow.getHours();
  if(s.innerHTML < 10){       s.innerHTML="0"+timeNow.getSeconds();
  }     
m.innerHTML=timeNow.getMinutes();
  if(m.innerHTML < 10){       m.innerHTML="0"+timeNow.getMinutes();
  }   
s.innerHTML=timeNow.getSeconds();
  if(s.innerHTML < 10){       s.innerHTML="0"+timeNow.getSeconds();
  }
},1000)