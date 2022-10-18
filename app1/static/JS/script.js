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
    let peso = document.querySelector("#sinalVital_peso");
    console.log(peso.value)
    let altura = document.querySelector("#sinalVital_altura");
    console.log(altura.value)
    let resultado = peso.value / (altura.value*altura.value);
    console.log(resultado)
    let arredondado = parseFloat(resultado).toFixed(2);
    console.log(arredondado)
    var input = document.querySelector("#id_sinalVital_IMC");
    var input2 = document.getElementById("id_sinalVital_temp");

    // arredondado = input.value.toFixed(2)
    
    arredondado = parseFloat(input.value).toFixed(2)

    if (arredondado >= 0 && arredondado!=Infinity) {
        input2.value = arredondado;
    } else {
        input2.value = 0;
    }
    
    
    let num = 5.56789;
    let n = num.toFixed(2);
    console.log(typeof(parseFloat(input.value)));

    // let peso = document.querySelector("#sinalVital_peso");
    // let altura = document.querySelector("#sinalVital_altura");
    // let resultado = peso / (altura*altura);
    // let arredondado = parseFloat(resultado).toFixed(2);
    // var input2 = document.getElementById("id_sinalVital_temp");
    // var IMC = document.getElementById("id_sinalVital_IMC");
    

    // arredondado = input.value.toFixed(2)
    
    
    // IMC.value = arredondado
    // input2.value = arredondado
    // let num = 5.56789;
    // let n = num.toFixed(2);
    // console.log(arredondado);
}