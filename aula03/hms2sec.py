def hms2sec(h, m, s):
    return s + m*60 + h*60*60

def sec2hms(s):
    horas=s//(60*60)
    minutos=(s//60) % 60
    segundos=s%60

    return horas, minutos, segundos



def main():
    h=1996
    m=1
    s=29

    sec=hms2sec(h, m, s)
    print(h, "horas,", m, "minutos e", s, "segundos correspondem a", sec, "segundos.")


    segundos=93629
    (h1, m1, s1)=sec2hms(segundos)
    print(segundos, "segundos correspondem a", h1, "horas,", m1, "minutos e", s1, "segundos.")

main()