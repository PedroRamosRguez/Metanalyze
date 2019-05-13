$('input[name=dataOutput]').change( (e) => {
	console.log($('input[type=  radio][name=dataOutput]:checked').next('span').text().trim());
	if($('input[name=dataOutput]:checked').next().text().trim() === 'Plot'){
		console.log('plot elegido')
		$('#xAxisChart').show();
	}else if($('input[name=dataOutput]:checked').next().text().trim() === 'Table and Plot'){
		console.log('table-plot elegido')
		$('#xAxisChart').show();
	}else{
		console.log('table elegido')
		$('#xAxisChart').hide();
	}
})
