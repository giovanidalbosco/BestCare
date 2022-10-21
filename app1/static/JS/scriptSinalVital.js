(function(){
    $("#tabsinalvital").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim-sinalvital").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalsinalvital").modal("show");
    });

    $("#btnsim-sinalvital").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/sinalvital_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/sinalvital_list";
            }
        });
    });
})();
