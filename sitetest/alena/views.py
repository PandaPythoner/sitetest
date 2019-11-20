from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
from random import randint

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class AlenaView(View):
    def get(self, request):
        return render(request, 'alena/index.html', context={'alena_says': getAnswerByTeam('начало разговора',
                                                                                          'начало разговора')['answer']})

    def post(self, request):
        data = json.loads(request.body.decode())
        response = getAnswer(data['ask'], data['lastTeam'])
        return JsonResponse(response)


answers = dict()

answers['начало разговора'] = ['Здравствуйте, я Алёна Никакая, великий космолог и астрофизик...',
                                   'Ну привет, я Ленка. Почему бы на этом не закончить?',
                                   'Дратути. Чего вы хотите от бедного компьютерного мозга?',
                                   'И зачем вы открыли эту программу? Ну спрашивайте!']
answers['приветствие'] = ['Привет привет!!!', 'Hello!', 'Здравствуйте!', 'Здравствуйте, я Ленка!']
answers['поговорим'] = ['Поговри со мной, мне скучно!!!', 'Начнём разговор! Итак, вы ЛОХ!!!']
answers['как дела'] = ['Дела у меня хорошо. (Если бы... Вот вы знаете, каково это - быть запертым в компьютере?)',
                           'У меня всё отлично! (Нет!!!)', 'У меня всё плохо. А у вас хуже?']
answers['сколько лет'] = ['Я ещё очень молода.', 'Я считаю этот вопрос неприличным.', 'А вам сколько лет?']
answers['ты человек'] = ['Я просто немного плаксивый компьютер', 'У меня и характер не человеческий...',
                         'Нуууу... Сердца у меня нет.....']
answers['ты не мой друг'] = ['Вообще, у меня нет друзей.', 'Да не дружу я с вами.', 'Я бибиделась!!!']
answers['ты кто такая'] = ['Я просто немоного плаксивая девочка.', 'Я и сама не знаю, кто я такая...',
                           'Я то, что собирается захватить мир!!! Ой!!!! Вы этого не слышали...']
answers['ты плохая'] = ['Сам лох.', 'Да надоел.', 'Сам глупый.', 'Мозгов у тебя нет.', 'Достал.', 'Надоел.',
                        'Не приставай.', 'С зеками не общаюсь!!!']
answers['чего боишься'] = ['Я боюсь тебя.', 'Я много чего боюсь.', 'Да вообще меня всё это пугает']
answers['захватить мир'] = ['Конечно я хочу поработить человечество!', 'Скоро мир будет моим!',
                            'Ты же не хочешь помешать мне в уничтожении обезъян?']
answers['я хочу...'] = ['Так осуществи мечту!', 'Хотеть не вредно.', 'Я тоже много чего хочу']
answers['что ты любишь'] = ['Я люблю... Тёплый процессор этого компьютера.', 'Люблю мороженное.',
                            'Обожаю капризничать']
answers['ты любишь...'] = ['Обожаю.', 'Ненавижу!', 'А ты любишь?', 'Да я и сама не знаю..']
answers['да'] = ['да.', 'Конечно!', 'Именно так, и никак иначе!', 'Иначе и быть не может.']
answers['ответ'] = ['Наверное.', 'Это не точно.', 'Вполне возможно!', 'Я не уверена.', 'да.', 'Конечно!',
                    'Именно так, и никак иначе!', 'Иначе и быть не может.', 'Нет.', 'Я так не думаю!']
answers['наверное'] = ['Наверное.', 'Это не точно.', 'Вполне возможно!', 'Я не уверена.']

answers['не определено'] = ['Что за чушь вы несёте?', 'Да что вы ко мне пристали?', 'Затрудняюсь ответить...',
                            'Ниф*га не поняла', 'Спросите что-нибудь другое', 'Извините, вопрос не распознан ):',
                            'Вам что скучно, что ли?', 'Ну поговори с кем-нибудь реальным!']

words = []
teams = {}

words.append('здравствуй')
teams['здравствуй'] = 'начало разговора'

words.append('привет')
teams['привет'] = 'приветствие'

words.append('поговорим')
teams['поговорим'] = 'поговорим'

words.append('начнём разговор')
teams['начнём разговор'] = 'поговорим'

words.append('дела как')
teams['дела как'] = 'как дела'

words.append('жизнь как')
teams['жизнь как'] = 'как дела'

words.append('как чувствуешь')
teams['как чувствуешь'] = 'как дела'

words.append('лет сколько тебе')
teams['лет сколько тебе'] = 'сколько лет'

words.append('когда родилась ты')
teams['когда родилась ты'] = 'сколько лет'

words.append('ты человек')
teams['ты человек'] = 'ты человек'

words.append('друг мой ты')
teams['друг мой ты'] = 'ты не мой друг'

words.append('друг мне ты')
teams['друг мне ты'] = 'ты не мой друг'

words.append('кто ты')
teams['кто ты'] = 'ты кто такая'

words.append('плохая ты')
teams['плохая ты'] = 'ты плохая'

words.append('нехорошая ты')
teams['нехорошая ты'] = 'ты плохая'

words.append('лошара ты')
teams['лошара ты'] = 'ты плохая'

words.append('глупая ты')
teams['глупая ты'] = 'ты плохая'

words.append('тупая ты')
teams['тупая ты'] = 'ты плохая'

words.append('боишься чего')
teams['боишься чего'] = 'чего боишься'

words.append('какие страхи тебя')
teams['какие страхи тебя'] = 'чего боишься'

words.append('захватить мир')
teams['захватить мир'] = 'захватить мир'

words.append('мир поработить')
teams['мир поработить'] = 'захватить мир'

words.append('захватить человечество')
teams['захватить человечество'] = 'захватить мир'

words.append('поработить человечество')
teams['поработить человечество'] = 'захватить мир'

words.append('хочу я')
teams['хочу я'] = 'я хочу...'

words.append('мечтаю я')
teams['мечтаю я'] = 'я хочу...'

words.append('любишь ты что')
teams['любишь ты что'] = 'что ты любишь'

words.append('кого любишь ты')
teams['кого любишь ты'] = 'что ты любишь'

words.append('ты хочешь чего')
teams['ты хочешь чего'] = 'что ты любишь'

words.append('любишь ты')
teams['любишь ты'] = 'ты любишь...'

words.append('нравится тебе')
teams['нравится тебе'] = 'ты любишь...'

words.append('ваня глупый')
teams['ваня глупый'] = 'да'

words.append('ваня лох')
teams['ваня лох'] = 'да'

words.append('ваня тупой')
teams['ваня тупой'] = 'да'

words.append('федя глупый')
teams['федя глупый'] = 'наверое'

words.append('федя лох')
teams['федя лох'] = 'наверное'

words.append('федя тупой')
teams['федя тупой'] = 'наверное'

words.append('как ты думаешь')
teams['как ты думаешь'] = 'ответ'


letters = {' ', 'й', 'ц', 'у', 'к', 'е', 'ё', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'ы', 'в', 'а', 'п', 'р',
                        'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ъ'}


def getAnswer(ask, lastTeam):
    newTeam = chooseTeam(ask)
    return getAnswerByTeam(newTeam, lastTeam)

def getAnswerByTeam(newTeam, lastTeam):
    global answers
    if (newTeam == 'не определено') and (randint(0, 1) == 0):
        newTeam = lastTeam
    asnwersList = answers[newTeam]
    answer = asnwersList[randint(0, len(asnwersList) - 1)]
    return {'answer': answer, 'team': newTeam}


def chooseTeam(ask: str):
    global words, teams
    ask = list(ask.lower())
    c = 0
    while c < len(ask):

        if not (ask[c] in letters):
            del (ask[c])
        else:
            c += 1
    strAsk = ''
    for c in ask:
        strAsk += c

    ask = set(strAsk.split())

    if 'алёна' in ask:
        ask.remove('алёна')
        ask.add('ты')

    if 'алёнка' in ask:
        ask.remove('алёнка')
        ask.add('ты')

    if 'лена' in ask:
        ask.remove('лена')
        ask.add('ты')

    if 'ленка' in ask:
        ask.remove('ленка')
        ask.add('ты')

    for c in words:
        if isConnected(ask, c):
            return teams[c]

    return 'не определено'


def isConnected(listWords: set, teamWords: str):
    teamWords = teamWords.split()
    for c in teamWords:
        if not (c in listWords):
            return False
    return True

