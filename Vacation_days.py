class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name  # Имя
        self.second_name = second_name  # Фамилия
        self.gender = gender  # Пол
        self.remaining_vacation_days = self.vacation_days  # Количество дней отпуска
    
    # Вычисляем количество дней отпуска доступных сотруднику
    def consume_vacation(self, missing_days):
        self.remaining_vacation_days -= missing_days
        
    # Печатаем сообщение с доступным количеством дней
    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)
print(employee.get_vacation_details())
