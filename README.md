# Page object models
## Обзор
В пользовательском интерфейсе вашего веб-приложения есть области, с которыми взаимодействуют ваши тесты. **Page Object** моделирует их только как объекты в тестовом коде. Это уменьшает количество дублирующегося кода и означает, что если пользовательский интерфейс изменится, исправление нужно будет применить только в одном месте.

**Page Object** — это шаблон проектирования, который стал популярным в автоматизации тестирования для улучшения обслуживания тестов и сокращения дублирования кода. **Page object** — это объектно-ориентированный класс, который служит интерфейсом для страницы вашего AUT. Затем тесты используют методы этого класса объекта страницы всякий раз, когда им нужно взаимодействовать с пользовательским интерфейсом этой страницы. Преимущество заключается в том, что если пользовательский интерфейс страницы изменяется, сами тесты не нужно менять, нужно изменить только код внутри объекта страницы. Впоследствии все изменения для поддержки этого нового пользовательского интерфейса располагаются в одном месте.

## Преимущества
* Существует четкое разделение между тестовым кодом и кодом, специфичным для страницы, таким как локаторы (или их использование, если вы используете карту пользовательского интерфейса) и макет.
* Для сервисов и операций, предлагаемых страницей, создан единый репозиторий, а не эти сервисы разбросаны по всем тестам.
