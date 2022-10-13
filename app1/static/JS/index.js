
//const modal = document.getElementById('modal');


//function toggleModal() {
//    modal.classList.toggle('modal-visible')
//}

 
(function(){
    $("#tabresidentes").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalresidente").modal("show");
    });

    $("#btnsim").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/residentes_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/residentes_list";
            }
        });
    });
})();


function exibir_ocultar(){
    var valor = $("#id_title").val();

    if(valor === '2'){
        $("#id_event_consumo_nome_label").show();
        $("#id_event_consumo_nome").show();
        $("#id_event_dose_label").show();
        $("#id_event_dose").show();

    } else {
        $("#id_event_consumo_nome_label").hide();
        $("#id_event_consumo_nome").hide();
        $("#id_event_dose_label").hide();
        $("#id_event_dose").hide();
    }
};