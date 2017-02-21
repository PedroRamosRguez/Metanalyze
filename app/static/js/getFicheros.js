/*Script para guardar en un array los ficheros que ha instroducido el usuario...*/
const ficheros = []

  const fileInput = $("#fichero")
  $("#introduceAlgoritmo").click(() =>{
  let input = fileInput.get(0);
    // Create a reader object
    let reader = new FileReader();
    if (input.files.length) {
        let textFile = input.files[0];
        // Read the file
        reader.readAsText(textFile);
        // When it's loaded, process it
        $(reader).on('load', processFile);
    } else {
        alert('Please upload a file before continuing')
    }
    ficheros.push(reader)
    console.log(ficheros)
    $("#introduceAlgoritmo").hide();
    $("#ficheroPruebas").hide();
  });
  console.log('probando fuera...')

processFile = (e) => {
    let file = e.target.result,
        results;
    if (file && file.length) {
        //results = file.split("\n");
        console.log(results)
    }
}

getFicheros = () =>{
  return ficheros
}