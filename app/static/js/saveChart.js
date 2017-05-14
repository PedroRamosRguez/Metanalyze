//dibuja el fondo blanco para descargarlo en png.
var backgroundColor = 'white';
Chart.plugins.register({
    beforeDraw: function(c) {
        var ctx = c.chart.ctx;
        ctx.fillStyle = backgroundColor;
        ctx.fillRect(0, 0, c.chart.width, c.chart.height);
    }
});

//se pasa a blob el chart para poder guardarlo.
$("#saveMinChart-btn").click(()=>{
	let chart=  $('.chart').get(0)
	chart.toBlob((blob) =>{
  		saveAs(blob,'MinChart.png')
	})
})
//boton para guardar el chart de avg
$("#saveAvgChart-btn").click(()=>{
	let chart=  $('.chart').get(1)
	chart.toBlob((blob) =>{
  		saveAs(blob,'AvgChart.png')
	})
})
//Boton para guardar el chart de Maximos
$("#saveMaxChart-btn").click(()=>{
	let chart=  $('.chart').get(2)
	chart.toBlob((blob) =>{
  		saveAs(blob,'MaxChart.png')
	})
})
//boton para guardar el chart de minavgmax
$("#saveMinAvgMaxChart-btn").click(()=>{
	let chart=  $('.chart').get(3)
	chart.toBlob((blob) =>{
  		saveAs(blob,'MinAvgMaxChart.png')
	})
})
/*
Para mergear todos, seguir este ejemplo...
http://stackoverflow.com/questions/29187029/save-multiple-canvas-as-one-image-make-website-like-picframe
*/