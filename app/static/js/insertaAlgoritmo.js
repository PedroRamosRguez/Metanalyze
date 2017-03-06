insertAlgorithms= (i) => {
  //funcion de jquery para comprobar que se tiene un array de botones.  
  $(`#btnAlgorithm${i}`).each(() => {

    let algorithmName = document.getElementById(`algorithm${i}`).value;
    console.log(algorithmName);
    console.log('le diii y soy el boton '+ i);

    //cambiar a remove para ver si no borra datos..
    $(`#btnAlgorithm${i}`).css("display","none");
    $(`#algorithm${i}`).css("display","none");
    $('#algorithmConfiguration').show();
  })
  
  
}