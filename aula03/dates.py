
# This function checks if year is a leap year.
# It is wrong: 1900 was a common year!
def isLeapYear(year):

    #só aceita argumentos de tipo "int"
    if isinstance(year, int)==False:
        return False

    #se o ano é divisível por 4, pode ser um ano bissexto, mas só se não for divisível por 100, ou se for, também tem que ser obrigatoriamente divisível por 400
    if year%4==0:
        if year%100!=0:
            return True
        elif year%100==0 and year%400==0:
            return True
        else:
            return False 
    else:
        return False


# This function has a semantic error: February in a leap year should return 29!
# Correct it.
def monthDays(year, month):

    #só aceita argumentos de tipo "int"
    if isinstance(year, int)==False or isinstance(month, int)==False:
        print("Argumentos inválidos.")
        exit()

    #verificar se o mês pertence ao calendário gregoriano
    if month<=0 or month>12:
        print("Argumento de mês não é válido.")
        exit()

    MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        # This tuple contains the days in each month (on a common year).
        # For example: MONTHDAYS[3] is the number of days in March.

    #verificar se mês é Fevereiro (que pode ter 29 ou 28 dias). Se não for, os dias já estão pré-determinados acima em MONTHDAYS
    if month==2:
        if isLeapYear(year)==True:
            days=29
        else:
            days=28
    else: 
        days = MONTHDAYS[month]
    return days

# This is wrong, too.
def nextDay(year, month, day):

    #só aceita argumentos de tipo "int"
    if isinstance(year, int)==False or isinstance(month, int)==False or isinstance(day, int)==False:
        print("Argumentos inválidos.")
        exit()

    #Se o dia for o último do mês, vamos ter alteração de mês (e o dia será o primeiro desse novo mês) e, em alguns casos, de ano também
    if day==monthDays(year, month):
        if month==12:
            return year+1, 1, 1
        else:
            return year, month+1, 1
    else: 
        day += 1
    return year, month, day

def dateIsValid(year, month, day):

    #só aceita argumentos de tipo "int"
    if isinstance(year, int)==False or isinstance(month, int)==False or isinstance(day, int)==False:
        return False

    #verificar se "month" pertence ao calendário gregoriano
    if month<=0 or month>12:
        return False

    #verificar se o mês contém pelo menos um número de dias menor ou igual ao argumento "day"
    if day<=0 or day>monthDays(year, month):
        return False
    return True

def previousDay(year, month, day):

    #só aceita argumentos de tipo "int"
    if isinstance(year, int)==False or isinstance(month, int)==False or isinstance(day, int)==False:
        print("Argumentos inválidos.")
        exit()

    #verificar se "month" pertence ao calendário gregoriano
    if month<=0 or month>12:
        print("Argumento de mês inválido.")
        exit()

    #verificar se o mês contém pelo menos um número de dias menor ou igual ao argumento "day"
    if day<=0 or day>monthDays(year, month):
        print("Argumento de dia inválido.")
        exit()

    #se o dia for o primeiro do mês, vamos ter alteração de mês, e possivelmente de ano também (e o novo dia passará a ser o último dia do mês anterior)
    if day==1:
        if month==1:
            return year-1, 12, 31
        else:
            return year, month-1, monthDays(year, month-1)
    else:
        return year, month, day-1


# This is the main function
def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?


    #Exercícios para avaliação ou coisa do género
    print("dateIsValide(1996, 1, 29):",dateIsValid(1996, 2, 29))
    print("previousDay(1995,3,1):", previousDay(1996,2,29))

# call the main function
main()
