(function(){
    $("#tabestoqueindividual").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim-estoque").attr("data-id",botaoClicado.attr("data-id"));
        $("#btnsim-estoque").attr("data-nome",botaoClicado.attr("data-nome"));
        $("#modalestoqueindividual").modal("show");
    });

    $("#btnsim-estoque").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        let nome = botaoSim.attr("data-nome");
        console.log(nome)
        $.ajax({
            url: "/estoque_individual_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/estoque_individual_list/?search=" + nome;
            }
        });
    });
})();
