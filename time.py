from datetime import datetime


def CurrentTime():
    t = datetime.now()
    
    print("Date: {}/{}/{} Time: {}:{}".format(t.day, t.month, t.year, t.hour, t.minute))


if __name__ == "__main__":
    CurrentTime()