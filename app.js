function AjaxZahtev(options, callback) {
  var req = new XMLHttpRequest();
  req.open(options.metod, options.putanja, true);
  req.addEventListener("load", function() {
    if (req.status < 400) {
 		  callback(req.responseText);
    }
    else {
 		  callback(new Error("Request failed: " + req.statusText));
    }
  });
  req.addEventListener("error", function() {
    callback(new Error("Network error"));
  });
  req.send(options.sadrzaj || null);
}

function PosaljiTvit(){
  var options = {}
  options.metod = "POST"
  options.putanja  = "novi-tvit"
  ime = document.getElementById("ime").value
  poruka = document.getElementById("tvit").value.slice(0,140)
  options.sadrzaj = JSON.stringify({"ime": ime, "tvit": poruka})
  AjaxZahtev(options, ProcesirajOdgovor)
  document.getElementById("tvit").value = ""
}

function ProcesirajOdgovor(odgovor){
  tvitovi = eval(odgovor)
  document.getElementById("moji-tvitovi").innerHTML = "<h4>MOJI TVITOVI</h4>"
  document.getElementById("pratim-tvitovi").innerHTML = "<h4>KOGA PRATIM: "+document.getElementById("pratim").value +"</h4>"
  pratim = document.getElementById("pratim").value.split(",") 
  for (i in tvitovi){
    tvit = JSON.parse(tvitovi[i])
    if (tvit.ime === document.getElementById("ime").value && tvit.tvit !== "")  
    	document.getElementById("moji-tvitovi").innerHTML += "<p>"+tvit.ime + ": "+ tvit.tvit+"</p>"
    //else if (tvit.ime === "all" || tvit.ime === document.getElementById("pratim").value)
    else if (document.getElementById("pratim").value === "all" || pratim.indexOf(tvit.ime) > -1)
      document.getElementById("pratim-tvitovi").innerHTML += "<p>"+tvit.ime + ": "+ tvit.tvit+"</p>"
  }
}
