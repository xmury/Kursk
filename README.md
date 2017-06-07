# 7 июня 2017
Функция test-paragraph должна проводить фильтрацию данных из тега <p>
Для извлечения необходииых параметров заведём переменную следующего вида:
    var = ["info" = {"num":2}]

Дана следующая выдача:
    *['2', '!!!', '<p', '', 'style="margin-bottom', '0.11in', 'line-height', '115%"><font', 'color="#404040"><font', 'face="Calibri,', 'serif"><font', 'size="2"', 'style="font-size', '11pt"><span', 'lang="en-US">Абзац</span></font></font></font><font', 'face="Calibri,', 'serif"><font', 'size="2"', 'style="font-size', '11pt"><span', 'lang="en-US">', '</span></font></font><font', 'color="#404040"><font', 'face="Calibri,', 'serif"><font', 'size="2"', 'style="font-size', '11pt"><span', 'lang="en-US">МИ']*

_Запись номера параграфа: if w == '!!!': var = ["info"]["num"] = предыдущее значение w

Теперь имеем следующий результат:
    ['2', '!!!', '<', 'p', '', 'style', 'margin-bottom', '0.11in', 'line-height', '115%>', '<', 'font', 'color', '#404040>', '<', 'font', 'face', 'Calibri,', 'serif>', '<', 'font', 'size', '2', 'style', 'font-size', '11pt>', '<', 'span', 'lang', 'en-US>', 'Абзац<', '/span>', '<', '/font>', '<', '/font>', '<', '/font>', '<', 'font', 'face', 'Calibri,', 'serif>', '<', 'font', 'size', '2', 'style', 'font-size', '11pt>', '<', 'span', 'lang', 'en-US>', '', '<', '/span>', '<', '/font>', '<', '/font>', '<', 'font', 'color', '#404040>', '<', 'font', 'face', 'Calibri,', 'serif>', '<', 'font', 'size', '2', 'style', 'font-size', '11pt>', '<', 'span', 'lang', 'en-US>', 'МИ', '1.15<', '/span>', '<', '/font>', '<', '/font>', '<', '/font>', '<', '/p>']

Попробуем разделить содержимое на теги. Для этого будем записывать то что лежит в промежутке от < до > будем записывать в отдельные списки
  
