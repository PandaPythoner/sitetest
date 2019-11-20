lastTeam = 'начало разговора';

function connect(url, json, onload_function){
    $.ajax({
        url: url,
        type: "POST",
        success: onload_function,
        error: function (error){
            alert('Error while connecting server: ' +  error.message);
        },
        dataType: "json",
        data: JSON.stringify(json)
    });
}

function ask_alena()
{
    ask = document.getElementById('inputtext').value;
    document.getElementById('inputtext').value = '';
    add_your_ask(ask);

    onl = function(response) {
        add_alena_answer(response.answer);
        lastTeam = response.team;
    };

    var data = {
        "ask": ask,
        'lastTeam': lastTeam,
    };

    connect('/alena/', data, onl);
}

function add_alena_answer(text){
    chat = document.getElementById('chat');
    answer = document.createElement("div");
    answer.className = 'messages alena_messages';
    answer.innerHTML = '<font size = "5">' + text + '</font><br/><font size = "1">Алёна</font>';
    answer.setAttribute('align', 'left');
    chat.appendChild(answer);
    chat.scrollTop = chat.scrollHeight;
}

function add_your_ask(text){
    chat = document.getElementById('chat');
    answer = document.createElement("div");
    answer.className = 'messages your_messages';
    answer.innerHTML = '<font size = "5">' + text + '</font><br/><font size = "1">Вы</font>';
    answer.setAttribute('align', 'right');
    chat.appendChild(answer);
    chat.scrollTop = chat.scrollHeight;
}
