class AnonymousSurvey():
    """Сбор анонимных ответов на опросы."""

    def __init__(self, quastion):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.quastion = quastion
        self.responses = []

    def show_quastion(self):
        """Выводит вопрос"""
        print(self.quastion)

    def store_response(self, new_response):
        """Сохраняет один ответ на опрос."""
        self.responses.append(new_response)

    def show_result(self):
        """Выводит все полученные ответы."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")