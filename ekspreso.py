def ekspreso():
    print('Инвентарь:\n- Кофемолка. (Лучше всего подойдет ручная. Также можно')
    print('использовать заранее перемолотый кофе.')
    print('- Турка.\n- Кастрюля.\n- Блюдце.\n- Приборы для кофепития.')
    print('Необходимые ингредиенты:\n- 2-3 ложки зернового или молотого кофе.')
    print('- 200 миллилитров фильтрованной воды.\n- 2-3 ложечки сахара.')
    print('- 1/5 чайной ложки соли.')
    ready = input()
    if ready == 'Да':
        print('Первый шаг:\nПеремолите зерна.')
        ready = input()
        if ready == 'Да':
            print('Второй шаг:\nВозьмите турку (0.25 мл) и насыпьте в нее 2-3')
            print('чайные ложечки молотой смеси, пару ложек сахара и немного')
            print('крупной поваренной соли.')
            print('Тщательно все перемешайте.\nПоставьте турку на огонь для прогревания')
            print('Держите турку на расстоянии нескольких сантиметров\n')
            print('над огнем и регульрно помешивайте, чтобы сухая смесь не пригорела.')
            print('Начните нагревать воду до 40 градусов.')
            ready = input()
            if ready == 'Да':
                print('Третий шаг:\nПосле полного прогревания смеси')
                print('(определить можно по исходящему от неё жару)')
                print('добавьте в неё заранее нагретую до 30-40 градусов воду')
                ready = input()
                if ready == 'Да':
                    print('Четвертый шаг:\nДоведите содержимое турки до кипения и')
                    print('сразу уберите с огня. Тщательно перемешайте смесь,')
                    print('чтобы поднявшаяся гуща снова оказалась под водой.')
                    print('Снова поставьте турку на огонь.')
                    ready = input()
                    if ready == 'Да':
                        print('Пятый шаг:\nПосле второго закипания уберите турку с огня')
                        print('и накройте блюдцем на 5-7 минут, чтобы смесь отстоялась.')
                        ready = input()
                        if ready == 'Да':
                            print('Домашний кофе эспрессо готов. Осталось перелить его')
                            print('в кофейную чашку, и можно приступать к употреблению.')
                            print('*При желании в кофе можно добавить корицу, взбитые')
                            print('сливки или молоко. Это придаст ему особенный вкус.')
    elif ready == 'нет, больше времени':
        pass
    else:
        pass  # выйти в главное меню из функции, законичить функцию, сделать что-нибудь!!!!!!!!!!!!!!!!!!!!!11111
    