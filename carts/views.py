from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from carts.forms import Events_form, Group_ops_form, Swap_carts
from carts.models import Events, Cartridge, Num

'''
def home(request):
    return render_to_response('cart_home.html', {'events': Events.objects.all().order_by('-date')})
'''
# places
store = 1
fill_station = 2
# statuses
working = 1
at_home = 2
gone_away = 3

# Главная. Форма ввода и вывод последних событий
@login_required
def home(request):
    # form = Events_form
    args = {}
    args.update(csrf(request))
    args['form'] = Events_form
    args['swap_form'] = Swap_carts
    args['Cartridge'] = Cartridge.objects.all().order_by('-last_datetime')
    args['username'] = auth.get_user(request).username
    args['url_name'] = request.resolver_match.url_name  # Передает css классу "active" имя текущей вкладки
    return render_to_response('cart_home.html', args)


@login_required()
def event_add(request):
    try:
        if request.method == 'POST':
            form = Events_form(request.POST)
            if form.is_valid():  # Проверка валидности формы
                get_status = int(request.POST.get('status'))
                get_num = int(request.POST.get('num'))
                get_place = int(request.POST.get('place'))

                if get_status == at_home:  # Проверка на статус "Приехал"
                    count = Cartridge.objects.get(num=get_num)  # Выяснение текущего к-ва заправок
                    count = count.fill_count + 1  # Инкремент к-ва заправок
                    Cartridge.objects.update_or_create(
                        num_id=get_num,
                        defaults=dict(num_id=get_num,
                                      status_id=get_status,
                                      place_id=get_place,
                                      fill_count=count)
                    )
                else:
                    Cartridge.objects.update_or_create(
                        num_id=get_num,
                        defaults=dict(num_id=get_num,
                                      status_id=get_status,
                                      place_id=get_place)
                    )
                # event = Events(status_id=get_status, num_id=get_num, place_id=get_place)
                # event.save()  # Сохарнение записи в евенты
                # print("ok else")
    except:
        pass

    return HttpResponseRedirect('/carts/cart_home/')


def homecoming(request, num_id):
    try:
        count = Cartridge.objects.get(num=num_id)  # Выяснение текущего к-ва заправок
        count = count.fill_count + 1  # Добавление еще одного раза
        car = Cartridge.objects.get(num_id=num_id)
        car.status_id = at_home
        car.place_id = store
        car.fill_count = count
        car.save()
        event = Events(status_id=at_home, num_id=num_id, place_id=store)
        event.save()  # Сохранение записи в евенты
    except ObjectDoesNotExist:
        raise Http404

    return HttpResponseRedirect('/carts/cart_home/')


def send_refill(request, num_id):
    try:
        car = Cartridge.objects.get(num_id=num_id)
        car.status_id = gone_away
        car.place_id = fill_station
        car.save()
        event = Events(status_id=gone_away, num_id=num_id, place_id=fill_station)
        event.save()  # Сохранение записи в евенты
    except ObjectDoesNotExist:
        raise Http404

    return HttpResponseRedirect('/carts/cart_home/')


# Смотреть все картриджи одного статуса
def watch_status(request, status_id):
    args = {'status': Cartridge.objects.filter(status=status_id)}
    return render_to_response('watch_status.html', args)


# Смотреть об одном картридже
def watch_one_num(request, num_id):
    args = {'cart': Cartridge.objects.get(num_id=num_id)}
    return render_to_response('watch_one_num.html', args)


def watch_place(request, place_id):
    args = {'carts': Cartridge.objects.filter(place_id=place_id)}
    return render_to_response('watch_place.html', args)


def watch_model(request, model_id):
    args = {'carts': Cartridge.objects.filter(num_id=model_id)}
    return render_to_response('watch_model.html', args)


def test(request):
    return render_to_response('test.html')


def group_ops(request):
    form = Group_ops_form
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('group_ops.html', args)


def get_group_ops(request):
    if request.method == 'POST':
        form = Group_ops_form(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            a = form.cleaned_data
            nums = a['nums'].split(',')
            for n in nums:
                try:
                    num_id = Num.objects.get(num=n).id
                    count = Cartridge.objects.get(num=num_id)  # Выяснение текущего к-ва заправок
                    count = count.fill_count + 1  # Добавление еще одного раза
                    car = Cartridge.objects.get(num_id=num_id)
                    car.status_id = at_home
                    car.place_id = store
                    car.fill_count = count
                    car.save()
                    event = Events(status_id=at_home, num_id=num_id, place_id=store)
                    event.save()  # Сохранение записи в евенты
                except ObjectDoesNotExist:
                    pass
    return HttpResponseRedirect('/carts/cart_home/')


def get_swap(request, **kwargs):
    if request.method == 'POST':
        form = Swap_carts(request.POST)
        if form.is_valid():
            a = form.cleaned_data
            # print(request.POST[Cartridge.num.id=""])
            print(a['nums'])
            b = request.GET.get('')
            print(b)
    return HttpResponseRedirect('/carts/cart_home/')
