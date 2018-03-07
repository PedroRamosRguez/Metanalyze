/*Script para guardar en un array los ficheros que ha instroducido el usuario...*/
const ficheros = [];
const fileInput = $('#file');
$('#introduceAlgorithm').click(() =>{
  let formData = new FormData();
  formData.append('file', $('#file')[0].files[0]);
  ficheros.push(formData);

});

getFicheros = () =>{
  return ficheros;
}