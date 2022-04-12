
//   $(function(){
    
//     //Agregar clase a Menu -- Por ahora no funciona
//     $('body.conferencia .navegacion-principal a:contains("Conferencia")').addClass('activo');
//     $('body.calendario .navegacion-principal a:contains("Calendario")').addClass('activo');
//     $('body.invitados .navegacion-principal a:contains("Invitados")').addClass('activo');

//       //Menu fijo
//       var windowHeight = $(window).height();
//       var barraAltura = $('.barra').innerHeight();
//       $(window).scroll(function(){
//           var scroll = $(window).scrollTop();
//           if(scroll > windowHeight){
//             $('.barra').addClass('fixed');
//             $('body').css({'margin-top': barraAltura + 'px'});
//           }else{
//             $('.barra').removeClass('fixed');
//             $('body').css({'margin-top':  '0px'});
//           }
//       })

      

    //   //Menu responsive
      
    //   $('.menu-movil').on('click', function(){
    //       $('.navegacion-principal').slideToggle();
    //   })

    //   $(window).resize(function() {
    //     var windowWidth = $(".barra").width();
    //     if (windowWidth > 755) {
    //       $(".navegacion-principal").css({ display: "block" });
    //     } else {
    //       $(".navegacion-principal").css({ display: "none" });
    //     }
    //   });

    $(function(){
      //programa de conferencias
      $('.filtro-cat a:first').addClass('activo');
      $('#apartamento').addClass('ocultar')
      $('#rancho').addClass('ocultar')
      $('.filtro-cat a').on('click', function(){
        $('.filtro-cat a').removeClass('activo');
        $('#apartamento').addClass('ocultar')
        $('#casa').addClass('ocultar')
        $('#rancho').addClass('ocultar')
        $(this).addClass('activo');
        $('.ocultar').hide();
        let enlace = $(this).attr('href');
        $(enlace).removeClass('ocultar');
        $(enlace).fadeIn(1000);
        return false; 
    });

      
});
