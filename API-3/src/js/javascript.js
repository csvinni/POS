$(document).ready(function(){
    $("#form-tarefa").on("submit", function(event){
        event.preventDefault();

        const descricao = $("#descricao").val();
        const prioridade = $("#prioridade").val();
        const concluida = $("#status").val() === "true";

        const novaTarefa = {
            id: Math.floor(Math.random() * 10000), 
            descricao: descricao,
            prioridade: prioridade,
            concluida: concluida
        };

        $.ajax({
            url: "http://127.0.0.1:8000/tarefas/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(novaTarefa),
            dataType: "json",
            success: function(resposta){
                alert("Tarefa criada com sucesso!");
                console.log("Tarefa:", resposta);
            },
            error: function(xhr){
                alert("Erro ao criar tarefa!");
                console.error("Erro:", xhr.responseText);
            }
        });
    });

    function carregarTarefas() {
        $.get("http://127.0.0.1:8000/tarefas/", function(tarefas) {
            const tabela = $("#tabela-tarefas");
            
            tarefas.forEach(function(tarefa) {
                const statusTexto = tarefa.concluida ? "Concluída" : "Não concluída";
                const linha = `
                    <tr>
                        <td>${tarefa.descricao}</td>
                        <td>${tarefa.prioridade}</td>
                        <td>${statusTexto}</td>
                        <td><button class="Botao-cad" onclick="excluirTarefa(${tarefa.id})">Excluir</button></td>
                    </tr>
                `;
                tabela.append(linha);
            });
        }).fail(function(){
            alert("Erro ao carregar tarefas!");
        });
    }

    carregarTarefas();
});
