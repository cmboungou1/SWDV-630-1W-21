class Use_Vacation_Time:
    def __init__(self, accumulated_v_time: int, requested_time: int):
        self.accumulated_v_time = accumulated_v_time
        self.requested_time = requested_time

    def get_result(self):
        result = ''
        vaca_apprl = self.accumulated_v_time - self.requested_time
        if vaca_apprl < 0 :
            result = "your vacation request was denied. You haven't accumulated the number of hours you are requesting."
        else:
            result = 'Your vacation request was approved!'
        return result

class Use_Sick_Leave:
    def __init__(self, accumulated_sl_time: int, requested_time: int):
        self.accumulated_sl_time = accumulated_sl_time
        self.requested_time = requested_time

    def get_result(self):
        result = ''
        sick_L_apprl = self.accumulated_sl_time - self.requested_time
        if sick_L_apprl < 0 :
            result = "your sick leave request was denied. You haven't accumulated the number of hours you are requesting."
        else:
            result = 'Your sick leave request was approved!'
        return result


class Get_Paycheck:
    def __init__(self, hours_worked: int, hourly_rate: int):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_result(self):
        return "Paycheck: ${}".format(self.hours_worked * self.hourly_rate)


class Facade:
    @staticmethod
    def use_vacation_time(*args) -> Use_Vacation_Time:
        return Use_Vacation_Time(*args)

    @staticmethod
    def use_sick_leave(*args) -> Use_Sick_Leave:
        return Use_Sick_Leave(*args)

    @staticmethod
    def get_paycheck(*args) -> Get_Paycheck:
        return Get_Paycheck(*args)


if __name__ == "__main__":
    use_vacation_obj = Facade.use_vacation_time(2, 5)
    use_sick_leave_obj = Facade.use_sick_leave(100, 40)
    get_paycheck_obj = Facade.get_paycheck(80, 15)

    print(use_vacation_obj.get_result())
    print(use_sick_leave_obj.get_result())
    print(get_paycheck_obj.get_result())