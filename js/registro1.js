
function Guardar(){
    
    var user=document.getElementById('usuario').value;
    var clave=document.getElementById('clave').value;
    var correo=document.getElementById('correo').value;
    var direccion=document.getElementById('direccion').value;
    var telefono=document.getElementById('telefono').value;

    var parametros = {
        "user": user,
        "clave":clave,
        "correo":correo,
        "direccion":direccion,
        "telefono":telefono,
      }

    $.ajax({
        data: parametros,
        url: "registrousuarios.php",
        type: 'post',
         beforeSend: function () {//elemento que queramos poner mientras ajax carga
           $("#resultado").html("Procesando, espere por favor...");
         },
         success: function (response) {//resultado de la función
          $("#resultado").html(response);
           }
        });
}
/*
function Actualizar(codigo){
    var useCod='usuario'+codigo;
    var claCod='clave'+codigo;
    var coCod='correo'+codigo;
    var noCod='nombre'+codigo;
    var user=document.getElementById(useCod).value;
    var clave=document.getElementById(claCod).value;
    var correo=document.getElementById(coCod).value;
    var nombre=document.getElementById(noCod).value;
    alert("Actualizando: "+user);
}

function Eliminar(codigo){
    alert("Eliminando: "+codigo);
}

*/
