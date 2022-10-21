(function(){
    $("#tabcomorbidades").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim-comorbidade").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalcomorbidades").modal("show");
    });

    $("#btnsim-comorbidade").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/comorbidades_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/comorbidades_list";
            }
        });
    });
})();
