let a="https://api.openweathermap.org/data/2.5/weather?q=jakarta&appid=37cbff9a10e2b8841d2b260033f6e111&units=metric&lang=id"
let btn=document.querySelector(".searchBtn");
let kota=document.querySelector(".cities");
let lembab=document.querySelector(".humid");
let angin=document.querySelector(".wind");
let city=document.querySelector(".searchCty");
let cuaca=document.querySelector(".weatherPic");
let suhu=document.querySelector(".temp");
btn.addEventListener("click",()=>{
  cities=city.value; a=`https://api.openweathermap.org/data/2.5/weather?q=${cities}&appid=37cbff9a10e2b8841d2b260033f6e111&units=metric&lang=id`
  d();
  
})
async function d(){
  let b=await fetch(a);
  let c=await b.json();
  kota.innerHTML=c.name;
  let buang = kota.innerHTML;
  if (buang == "undefined"){
    kota.innerHTML="Insert another city";

  }
  
  angin.innerHTML=c.wind.speed+"KM/H";
lembab.innerHTML=c.main.humidity+"%";
  suhu.innerHTML=c.main.temp+"°C";
  if (true){
    cuaca.style.height="15rem";
    cuaca.style.margin="3rem";

  }
  if (c.weather[0].main == "Clouds"){
    cuaca.src="cloud.png";
    
  
}
  else if (c.weather[0].main == "Rain" || c.weather[0].main == "Drizzle"){
    cuaca.src="rain.png";
    

  }
  else if (c.weather[0].main == "Clear"){
    cuaca.src="clear.png";


  }
  else if (c.weather[0].main == "Mist"){
    cuaca.src="mist.png";


  }
  else if (c.weather[0].main == "Thunderstorm"){
    cuaca.src="thunder.png";


  }
  
  else if (c.weather[0].main == "Snow"){
    cuaca.src="snow.png";


  }}
  


  
  
  
d();



