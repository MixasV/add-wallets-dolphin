# dolphin-import-wallets-WIN

# Скрипт не мой

Добавил только возможность импорта в кошельки Keplr и Sui

!!!Версия скрипта для пользователей Windows, Смотрите инструкцию https://youtu.be/b8BMxROrQjo

данный скрипт импортирует заранее созданные метамаски в твои готовые профили в dolphin anty. скрипт написан на скорую руку, для меня было главное чтобы все работало. после импорта он добавляет сети optimism, bsc и arbitrum в кошелек. К сожалению, пока не сохраняет в отдельный файл адреса кошельков из ММ. В Кеплере и Sui реализовал.

1. экспортируй ids из dolphin со своих профилей. (есть скирипт для этого в моём профиле)
2. добавляешь эти ids в файл id_users.txt
3. добавляешь сид фразы от заранее созданных кошельков в файл seeds.txt
4. меняешь в файле ******.py переменную password (для создания кеплера ещё меняем там же "имя профиля")
5. скачиваем chromedriver той же версии, что и в профилях долфина.
6. Прописываем к нему путь в скрипте
7. Меняем ссылки к .txt файлам в скрипте на свои
8. запускаешь файл main.py - для импорта Метамасков (keplr.py для импорта Keplr, sui.py длф Sui). Кто не знает - сиды можно использовать те же

Рекомендую руками открыть окно с метамаском и проверить какая ссылка в браузере, а какая в скрипте. Иногда почему-то они разные. Скопируйте ту, по которой у вас открывается метамаск. То же может случиться и с кеплером.

Естественно, расширения должны быть предварительно установлены во все профили долфина.

не забудь заранее войти в свой dolphin, скрипт работает именно через него. 

библиотеки для скачивания : 
pip install selenium, requests, pyperclip, termcolor

Иногда, видимо из-за долгой загрузки страниц и происков гремлинов, скрипт сбивается и отключается. Так что не стоит просто поставить 100 акков на заполнение и идти пить чай. Может после 10 акков где-то не успеть прогрузиться стр. или тормознуть сама сеть кошелька и скрипт выдаст ошибку и остановится. Так что лучше поглядывать на него. Но буфер обмена при его работе лучше не использовать. Так как скрипт активно его юзает для своих задач.

P. S. Думаю, со временем, скрипт дополню другими кошельками. Так как принцип импорта у всех один, по сути.
