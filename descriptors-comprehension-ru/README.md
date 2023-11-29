# Мой разбор дескрипторов и объектов property
## Что такое property?
По соглашению, для доступа к атрибутам нужно определять специальные методы для чтения, записи и удаления, которые называются геттеры, сеттеры и делитеры.

Объекты property предоставляют API для использования сеттеров, геттеров и делитеров, через одно имя — обычно это имя существующего атрибута или новое имя для вычисляемого значения. 

При обращении к объекту property активируется нужный метод, где может быть определена дополнительная логика для доступа к атрибуту. Например, валидация, какое-либо ограничение и тп.

Объект property можно использовать двумя способами: при помощи функции ```property()``` или одноименного декоратора.

## Что такое дескрипторы?
Дескрипторы обеспечивают альтернативный способ управления доступом
к атрибутам. 

Фактически объекты property предоставляют более простой API для работы с дескрипторами.

Дескрипторы создаются как независимые классы и присваиваются атрибутам
класса. При попытке чтения, записи или удаления определенного атрибута вызывается соответствующий метод класса. Таким образом в этих методах можно задать дополнительную логику.

Обращение к дескриптору через точку активирует геттер, попытка присвоить значение активирует сеттер. Директива ```del``` активирует делитер.

Дескрипторы класса можно вызвать в конструкторе, тем самым при создании объекта, его атрибуты будут инициализированы через дескрипторы.

Протокол дескриптора включает методы ```__get__(), __set__() и __delete__()```, где задается логика при чтении, записи или удалении атрибута.

Еще можно переопределить метод ```__set_name__```, чтобы имя атрибута динамически изменялось. В этом методе создается локальный атрибут дескриптора, который может быть использован в качестве имени при создании, чтении и удалении атрибутов.