from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра AnonymousSurvey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_quastion()
print("Enter 'q' at any time to quit.\n")
while True:
    resource = input("Language: ")
    if resource == 'q':
        break
    my_survey.store_response(resource)

# Вывод результатов опроса.
print("\nThank you to everyone who participate in the survey!")
my_survey.show_result()