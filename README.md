# 7 июня 2017
Функция test-paragraph должна проводить фильтрацию данных из тега <p>
Для извлечения необходииых параметров заведём переменную следующего вида:
    var = ["info" = {"num":2}]

Дана следующая выдача:
    *['2', '!!!', '<p', '', 'style="margin-bottom', '0.11in', 'line-height', '115%"><font', 'color="#404040"><font', 'face="Calibri,', 'serif"><font', 'size="2"', 'style="font-size', '11pt"><span', 'lang="en-US">Абзац</span></font></font></font><font', 'face="Calibri,', 'serif"><font', 'size="2"', 'style="font-size', '11pt"><span', 'lang="en-US">', '</span></font></font><font', 'color="#404040"><font', 'face="Calibri,', 'serif"><font', 'size="2"', 'style="font-size', '11pt"><span', 'lang="en-US">МИ']*

_Запись номера параграфа: if w == '!!!': var = ["info"]["num"] = предыдущее значение w

Теперь имеем следующий результат:
    ['2', '!!!', '<', 'p', '', 'style', 'margin-bottom', '0.11in', 'line-height', '115%>', '<', 'font', 'color', '#404040>', '<', 'font', 'face', 'Calibri,', 'serif>', '<', 'font', 'size', '2', 'style', 'font-size', '11pt>', '<', 'span', 'lang', 'en-US>', 'Абзац<', '/span>', '<', '/font>', '<', '/font>', '<', '/font>', '<', 'font', 'face', 'Calibri,', 'serif>', '<', 'font', 'size', '2', 'style', 'font-size', '11pt>', '<', 'span', 'lang', 'en-US>', '', '<', '/span>', '<', '/font>', '<', '/font>', '<', 'font', 'color', '#404040>', '<', 'font', 'face', 'Calibri,', 'serif>', '<', 'font', 'size', '2', 'style', 'font-size', '11pt>', '<', 'span', 'lang', 'en-US>', 'МИ', '1.15<', '/span>', '<', '/font>', '<', '/font>', '<', '/font>', '<', '/p>']

Попробуем разделить содержимое на теги. Для этого будем записывать то что лежит в промежутке от < до > будем записывать в отдельные списки.

# 8 June 2017

Закончена работа над функцией test_paragraph(). Работа выглядит так:
    - **Вход.** Файл data.html
    - **Процесс.** Извлечение из него характеристик и предоставление интерфейса для доступа к ним.
    - **Выход.** Словарь славаря в словаре... Доступ осуществляется следующим образом: *data_paragraph\[Номер Абзаца\]\[Под-тег\]\[Параметр\]*   

Пришёл черед переделать под такой же интерфейс функцию test_style()
