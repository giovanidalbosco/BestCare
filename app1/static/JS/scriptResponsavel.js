(function(){
    $("#tabresponsavel").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim-responsavel").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalresponsavel").modal("show");
    });

    $("#btnsim-responsavel").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/responsavel_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/responsavel_list";
            }
        });
    });
})();
