function exibir_ocultar(){
    var valor = $("#id_title").val();

    if(valor === '1'){
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
