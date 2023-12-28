let re=document.querySelector(".atas");
const onscr=document.querySelectorAll(".os");
const acu=document.querySelector(".ac");
const de=document.querySelector(".de");
const tot=document.querySelector(".total");

let html="";


acu.addEventListener("click",()=>{
  acum();
})
de.addEventListener("click",()=>{
  dem();
})
tot.addEventListener("click",()=>{
  tut();
})

for(const cro of onscr){
  cro.addEventListener("click",()=>{
    html+=cro.innerHTML;

    onscren();
  })
}
function onscren(){
  re.innerHTML=html;
}
function acum(){
  re.innerHTML="";
  html="";

}
function dem(){
  html=html.slice(0,-1);
  re.innerHTML=html;
}
function tut(){
  if (html == ""){
    re.innerHTML="";
    
  }
  
  
  else{
    
    html=eval(html);
    re.innerHTML=html;
  }
  
  
  
}
