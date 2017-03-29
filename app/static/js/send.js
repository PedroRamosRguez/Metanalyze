/*Sript para realizar el envío de la configuración del usuario al servidor mediante una petición ajax
En la petición, se envían cada uno de los valores que el usuario introdujo en la pantalla de configuración.*/

//fucion para obtener el csrtoken de django
getCookie = (name) => {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
	for (var i = 0; i < cookies.length; i++) {
	  var cookie = jQuery.trim(cookies[i]);
	// Does this cookie string begin with the name we want?
	  if (cookie.substring(0, name.length + 1) == (name + '=')) {
	    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	    break;
	  }
	}
  }
 return cookieValue;	
}
//función Jquery que obtiene los diferentes datos que el usuario introdujo y realiza la petición ajax.
$("#formulario").submit(() =>{
	//Prepare csrf token
	var csrftoken = getCookie('csrftoken');
	let alg = getAlgorithms();
	let fich = getFicheros();
    let formData = new FormData();
    formData.append('csrfmiddlewaretoken',csrftoken)
    formData.append('nAlgorithms',document.getElementById('nAlgorithms').value)
    formData.append('algorithms',JSON.stringify(alg))
    formData.append('test',$('#test').val())
    formData.append('dataOutput',$('input[name=dataOutput]:checked').val())
    formData.append('nObjectives',document.getElementById('nObjectives').value)
    formData.append('nExecutions',document.getElementById('nExecutions').value)
    formData.append('step',document.getElementById('step').value)
    formData.append('stopCondition',document.getElementById('stopCondition').value)
    formData.append('bound',$('#bound').val())
    formData.append('metric',$('#metric').val())
   //bucle para añadir el array de ficheros que se generen por cada algoritmo
    fich.forEach(item => {
		for (var key of item.entries()) {
        	//console.log(key[0] + ', ' + key[1]);
        	formData.append(key[0],key[1])
    	}
	})
	$.ajax({
		//hasta poner esto era funcionaba sin problemaaaasss
		type:'POST',
		url : 'pruebatemplate/',
		contentType:false,
		cache: false,
		processData: false,
		datatype: 'json',
		data:formData,
		//si la petición es exitosa realiza la redirección	 
		success : function(data,textStatus){
		  //hace posible la redirección a la vista pruebatemplate...
		  window.location.href = 'pruebatemplate/'; 
		},
		//en caso de que la petición sea errónea, muestra el error de manera detallada.
		error : function(xhr,errmsg,err) {
		  console.log('hubo un error');	
 		  console.log(xhr.status + ": " + xhr.responseText); // muestra mejor información del error 
 		}
	});
	return false;
  })

