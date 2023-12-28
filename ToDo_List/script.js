let aktivitas=document.querySelector(".aktivitas");
let outer=document.querySelector(".outerBox");
let tombol=document.querySelector(".nambah");
let isi=document.querySelector(".isiAktivitas");
let a=0;
tombol.addEventListener("click",()=>{
  a+=1
  todoList()
});




function todoList(){
  let value=aktivitas.value;
  isi.innerHTML+=`<div id="par${a}" class="isiDiv"><div class="kalimat">${value}</div><button id="hilang${a}" class="Isitombol">x</button></div>`
  for (let i=1;i<=a;i++){
    document.getElementById(`hilang${i}`).addEventListener("click",()=>{
      document.getElementById(`hilang${i}`).style.display="none";
      document.getElementById(`par${i}`).style.display="none";

  
  })                      }}
