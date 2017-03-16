/*Script para guardar en un array los ficheros que ha instroducido el usuario...*/
const ficheros = [];
const fileInput = $('#file');
$('#introduceAlgorithm').click(() =>{
//let input = fileInput.get(0);
  // Create a reader object
  //let reader = new FileReader();
  let formData = new FormData();
  console.log(formData)
  //formData.append('file',$('#file')[0].files[0])
  formData.append('file', $('#file')[0].files[0]);
  //console.log(formData)
  ficheros.push(formData)
  //console.log(formData.getAll('file'))
  //console.log(ficheros2)
});
console.log('probando fuera...');

getFicheros = () =>{
  return ficheros;
}