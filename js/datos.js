function Ingresar(){
  var user=document.getElementById('usuario').value;
  var cla=document.getElementById('clave').value;

  var parametros = {
      "user": user,
      "clave":cla,
    }

  $.ajax({
      data: parametros,
      url: "validar.php",
      type: 'post',
       beforeSend: function () {//elemento que queramos poner mientras ajax carga
         $("#resultado").html("Procesando, espere por favor...");
       },
       success: function (response) {//resultado de la función
        $("#resultado").html(response);
         }
      });
}
