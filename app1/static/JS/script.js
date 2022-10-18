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



// $(document).ready(function () {
//     $('.mask-IMC').mask('99.99');
// });

function arredondar(){
    var input = document.querySelector("#id_sinalVital_IMC");
    var input2 = document.getElementById("id_sinalVital_temp");

    // arredondado = input.value.toFixed(2)
    
    arredondado = parseFloat(input.value).toFixed(2)

    input2.value = 34.345345
    let num = 5.56789;
    let n = num.toFixed(2);
    console.log(arredondado);
}