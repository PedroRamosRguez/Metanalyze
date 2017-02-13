/*Script para comprobar que el numero de instancias es de 1-99 y muestra un mensaje tipo span 
mostrando un error...*/

compruebaInstancia = () => {
  let instancia = document.getElementById("nInstancia").value;
  console.log(instancia)
  if(instancia.match(/^[1-9][0-9]{0,1}$/)){
    $("#spanPrueba").css("display", "none");
    $("#nInstancia").css("color","inherit")
    console.log('acepto...')
    $("#introduceInstancia").show();
  }else{
    console.log('no acepto')
    $("#nInstancia").css("color","#FF0000")
    $("#spanPrueba").css("display", "inherit");
    $("#introduceInstancia").hide();
  }
}