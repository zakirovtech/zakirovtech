# Quick start

## Windows

Для вызова клиента в терминале можно перейти в директорию, где располагается клиент:

```>> cd mysql\mysql server 8.0\bin
```

- Лучше всего добавить путь до директории с файлом исполнения в переменную окружения PATH, чтобы вызывать mysql в терминале с без привязки кдиректории.
 
Для запуска сервера вручную, нужно запустить командную строку от имени администратора и вызвать:
```
>> net start mysql 
>> net stop mysql
```
Подключение к серверу MySQL с правами пользователя root и паролем на localhost:3306:
```
>> mysql -u root -p
```
- root — имя администратора. Пароль для админа задается при 
установке, как и порт по умолчанию, где будет запускаться сервер — 3306.

## Linux

```
$ sudo apt update 
$ sudo apt upgrade

```
Ubuntu:
```
$ sudo apt install mysql-server
```
- В Kali используется MariaDB (база на основе MySQL — улучшенная MySQL):

```
$ sudo apt install default-mysql-server
```

Состояние сервера:
```
$ sudo service mysql status
```

Запустить / Остановить / Перезагрузить сервер:
```
$ sudo service mysql start / stop / restart или
$ sudo systemctl enable mysql — сервис будет запускаться при каждом запуске ОС
```

По умолчанию учетная запись root ставится без пароля. Для дальнейшей работы, нужно настроить root и установить ему пароль:
```
$ sudo service mysql start
$ sudo mysql
$ mysql> @ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'set_password_here';   
$ mysql> exit
```

Далее нужно запустить настройку безопасности:
```
$ sudo mysql_secure_installation
```

Далее можно войти как рут и создать базу и пользователя:
```
$ mysql -u root -p
```

# Команды после подключения 
Показать все доступные для пользователя на сервере базы:
```
>> show databases;
```

Поиск информации на сервере, используя таблицу переменных:
```
>> show variables like ‘somename’;

```
Создать новую базу данных:

```
>> create database <dbname>;
```

Выбрать нужную базу:

```
>> use <dbname>;
```

Показать все таблицы выбранной базы:

```
>> show tables 
```

Команда для создания нового user, после подключения как root:

```
>> CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
```

Все user доступны в таблице user базы mysql:

```
>> SELECT * FROM mysql.user;
```
## Привилегии

После создания user нужно дать ему привилегии (создавать, изменять или только забирать данные и тд.):

- All — все доступные привилегии

```
>> GRANT <SELECT, CREATE, UPDATE... or ALL> ON dbname.tablename TO 'user'@'localhost';
```

- .* — все таблицы

Увидеть предоставленные для пользователя привилегии:

```
>> SHOW GRANTS FOR 'user'@'host';
```

