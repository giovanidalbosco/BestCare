(function(){
    $("#tabmedicamentos").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim-medicamentos").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalmedicamentos").modal("show");
    });

    $("#btnsim-medicamentos").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/medicamentos_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/medicamentos_list";
            }
        });
    });
})();
