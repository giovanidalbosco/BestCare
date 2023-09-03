function exibir_ocultar(){
    var valor = $("#id_title").val();

    console.log(valor)

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


function calculo_IMC(){
    let peso = document.querySelector("#sinalVital_peso");
    let altura = document.querySelector("#sinalVital_altura");
    let resultado = peso.value / (altura.value*altura.value);
    let arredondado = parseFloat(resultado).toFixed(2);

    let input2 = document.getElementById("id_sinalVital_IMC");

    if (arredondado >= 0 && arredondado!=Infinity) {
        input2.value = arredondado;
    } else {
        input2.value = 0;
    }
}