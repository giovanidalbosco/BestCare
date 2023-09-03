(function(){
    $("#tabocorrencias").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim-ocorrencias").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalocorrencias").modal("show");
    });

    $("#btnsim-ocorrencias").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/ocorrencias_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/ocorrencias_list";
            }
        });
    });
})();
