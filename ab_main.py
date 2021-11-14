#import matplotlib.pyplot as plt #to display
import datetime as dt

# 날짜와 항목을 구분하는 함수
def dateFinder(line) :

    global date_check

    try :
        date = dt.datetime.strptime(line,'%Y/%m/%d').date()
        date_check = 1
        return date
    except :
        date_check = 0
        return line

#일별 금액의 합을 위한 임시변수
sum = 0

#날짜 구분을 위한 변수
date_check = 0

#월 총금액 및 평균금액
month_total = 0
month_avg = 0

# 날짜별 저장하기 위한 클래스
class DateList :

    def __init__(self) :
        self.datesum = {}
        self.item = {}

"""
day, list = 31, 10
dateList = [[NULL for j in range(list)] for i in range(day)]
"""

#파일 읽어오기
f = open('account_data.txt', 'r')#.read()

while True:
    line = f.readline()
    if not line: break
    data = dateFinder(line.strip())
    #print('1{} {}'.format(data, type(data)))


# 날짜별로 구분하여 항목명과 금액을 저장
    #먼저 날짜인 경우 데이터를 저장할 객체를 생성한다
    if date_check :
        Account = DateList()
        date = str(data)
        Account.datesum[date] = 0

        #날짜가 바뀌면 일별 항목 총금액을 더해준다.
        month_total += sum

        sum = 0
        print(data)

    #날짜가 아닐 경우 생성한 객체에 데이터 저장
    else :
        try :
            key, item = data.split()
            int_item = -1*int((item.replace('-','')).replace(',',''))
            print('{} : {}원'.format(key, item))

        #날짜가 줄바꿈으로 구분되어 있어 split()하지 못하는 입력이 오면 실행
        except :
            print('총사용액 : {}원\n'.format(Account.datesum[date]))


        #항목별 데이터 저장
        Account.item[key] = item

        #날짜별 사용금의 합 저장
        sum += int_item
        Account.datesum[date] = sum



#마지막 일별 총사용금까지 더해주기 위해
month_total += sum

# 평균사용금액을 저장.
month_avg = month_total // (int(date.replace('-',''))%100)

print('총사용액 : {}원\n'.format(Account.datesum[date]))
print('\n한달 총사용액 : {}원\n하루 평균사용액 : {}원\n'.format(month_total, month_avg))

# 평균사용금액을 넘는 날짜를 저장.

# 월별 모든 항목중에 가장 금액이 큰 항목을 저장.

# display창에 날짜별 모든 항목과 일별, 월별평균사용금과 월총액을 출력.

f.close()

# 다음에 구현예정
# 이 모든 것들을 display창에 달력의 형태로 출력.
    # 일별 총금액은 날짜별로 출력
    # 일별평균사용금, 월별평균사용금, 월별총액 등을 오른쪽에 출력
    # 월별평균사용금을 넘는 날짜는 붉은색으로 출력
