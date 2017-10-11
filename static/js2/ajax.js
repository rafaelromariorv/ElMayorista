
var proceso = new Object();
proceso.tipoPro = 1;
proceso.producto = new Array();
var table = new Array();
var cliente = new Object();

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

          cliente.dni = json[i].dni;
          cliente.nombre = json[i].nombre;
          cliente.apellidos = json[i].apellidos;

        }
        $('#clientes').html(html);
      }
    })
  })

$("#c-seleccionar").click(function(){
  proceso.clienProv = cliente.dni;
  $("#c-dni").text(cliente.dni);
  $("#c-nombre").text(cliente.nombre);
  var tipoPago = $("#f-tipoPago").val();
  var idMaquina = $("#f-maquinaid").val();
  proceso.tipoPago = tipoPago;
  proceso.idMaquina = idMaquina;
  //alert(texto);
  //alert(textot);
})


/*productos ajax*/
$('#p-buscar').submit(function(e){
  e.preventDefault();
  $.ajax({
    url: $(this).attr('action'),
    type: $(this).attr('method'),
    data: $(this).serialize(),
    success: function(json){
      console.log(JSON.stringify(json))
      var html = ""
      for (var i = 0; i < json.length; i++) {
        html += 'Codigo: '+json[i].fields.codigo + '<br>';
        html += 'elemento: '+json[i].fields.elemento + '<br>';
        html += 'valor Venta: '+json[i].fields.valorVenta + '<br>';
        html += 'IVA: '+json[i].fields.valorIva + '<br>';
        html += '<input name="p-cantidad" id="p-cantidad" type="number" min="1" max="200" step="1" value=1 autocomplete="off" required="required">';

        var fila = new Object();
        fila.codigo = json[i].fields.codigo;
        fila.elemento = json[i].fields.elemento;
        fila.valorVenta = json[i].fields.valorVenta;
        fila.valorIva = json[i].fields.valorIva;
        fila.cantidad = 1;

        table.push(fila);

      }
      $('#productos').html(html);
    }
  })
})

$("#p-seleccionar").click(function(){
  var d = table;
  var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
  var rowCount = t.rows.length;
  var row = t.insertRow(rowCount);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  var cell4 = row.insertCell(3);
  var cell5 = row.insertCell(4);
  var cell6 = row.insertCell(5);

  cell1.innerHTML = d[d.length-1].codigo;
  cell2.innerHTML = d[d.length-1].elemento;
  cell3.innerHTML = d[d.length-1].valorVenta - d[d.length-1].valorIva;
  d[d.length-1].cantidad = $('#p-cantidad').val();
  cell4.innerHTML = d[d.length-1].cantidad;
  cell5.innerHTML = d[d.length-1].valorIva * $('#p-cantidad').val();
  cell6.innerHTML = (d[d.length-1].valorVenta- d[d.length-1].valorIva)* $('#p-cantidad').val() +
                    d[d.length-1].valorIva * $('#p-cantidad').val();
  cell1.setAttribute('align','center');
  cell3.setAttribute('align','center');
  cell4.setAttribute('align','center');
  cell5.setAttribute('align','center');
  cell6.setAttribute('align','center');

  proceso.producto.push({'codigo': d[d.length-1].codigo, 'cantidad': d[d.length-1].cantidad});
  calTotal();
})

})//principal

//funciones aparte

function onEnviar(){
    //proceso.serie = $('#p-serie').val();
    //proceso.numero = $('#p-num').val();
    console.log(JSON.stringify(proceso));
    document.getElementById("proceso").value=JSON.stringify(proceso);
}

var total = 0;
function calTotal(){
    var total=0;
    var t=0;
    $('#tb-detalle tbody tr').each(function () {
        total = total*1 + $(this).find("td").eq(5).html()*1;
        t = t*1 + $(this).find("td").eq(4).html()*1;

    });
    $('#sum-subtotal').text((total));
    $('#sum-tax').text(t.toFixed(2));
    $('#sum-total').text(total+t);
}
