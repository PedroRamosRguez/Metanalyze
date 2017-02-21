function getCookie(name) {
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

$("#enviar").click(function(e) {
	//Prevent default submit. Must for Ajax post.Beginner's pit.
	e.preventDefault();
	//Prepare csrf token
	var csrftoken = getCookie('csrftoken');
	//console.log('le di al envio...')
	let alg = getAlgoritmos();
	let fich = getFicheros();
	console.log(fich)
	$.ajax({
		type:"POST",
		url: "pruebatemplate/",
		data:{csrfmiddlewaretoken : csrftoken,
			  algoritmo : alg,
			  test : $('#test').val(),
			  nInstancias : $('#nInstancia').val(),
			  nejecuciones : $('#nejecuciones').val(),
			 },
		success : function(data,textStatus){
		  console.log('exito..');
		  window.location.href = 'pruebatemplate/';
		 /* if(data.redirect){
		  	console.log('hay redirect...')
		  	
		  }else{
		  	console.log('no hay redirect..')
		  }*/
		  //console.log(data)
		},
		error : function(xhr,errmsg,err) {
		  console.log('hubo un error')	
 		  console.log(xhr.status + ": " + xhr.responseText); // muestra mejor información del error 
 		}
	})
  })

