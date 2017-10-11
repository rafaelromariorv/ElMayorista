
$(document).ready(function(){
  $("#search-proveedores").submit(function(e){
    e.preventDefault();
    $.ajax({
      url: $(this).attr('action'),
      type: $(this).attr('method'),
      data: $(this).serialize(),
      success: function(json){
        console.log(json)
        var html = ""
        if(json.length !=0){
          for (var i = 0; i <json.length; i++) {
            html += '<tr><td>'+json[i].id+ '</td><td>'+
  						json[i].nombreEmpresa+ '</td><td>'+
  						json[i].nombreRepresentante+'</td></tr>'
          }
          $("#datosC").html(html);
        }
        else {
          var msg = 'No existe provedores relacionados con el dato.'
          alert(msg);
        }
      }
    })
  })

$('#c-buscar').submit(function(e){
  e.preventDefault();
  $.ajax({
    url: $(this).attr('action'),
    type: $(this).attr('method'),
    data: $(this).serialize(),
    success: function(json){
      console.log(json)
      var html = ""
      for (var i = 0; i < json.length; i++) {
        html += 'DNI: '+json[i].dni + '<br>';
        html += 'nombres: '+json[i].nombre + '<br>';
        html += 'apellidos: '+json[i].apellidos + '<br>';
      }
      $('#clientes').html(html);
    }
  })
})

})
