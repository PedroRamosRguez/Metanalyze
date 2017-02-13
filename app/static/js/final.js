const prueba = []
const prueba2 = []
const fileInput = $("#fichero")
$("#introduceAlgoritmo").click(() =>{
  let alg = insertaAlgoritmo()
  prueba.push(alg)
  console.log(prueba)
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
  $("#introduceAlgoritmo").hide();
  $("#ficheroPruebas").hide(); 
  prueba2.push(reader)
  console.log(prueba2)
});
function processFile(e) {
    let file = e.target.result,
        results;
    if (file && file.length) {
        //results = file.split("\n");
        console.log(results)
    }
}

