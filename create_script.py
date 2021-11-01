# python manage.py shell
from home.models import Category, MyUser, Post, File, Comment

# 1) Category 샘플 데이터 추가
Category(code='1', category='윈도우 센서').save()
Category(code='2', category='연동 오류').save()
Category(code='3', category='주소 설정').save()
Category(code='4', category='회원 정보').save()
Category(code='5', category='기타 문의').save()
Category(code='6', category='리뷰').save()


# 2) MyUser 샘플 데이터 추가
MyUser(username='asef1125', first_name='나규륜', email='asef@naver.com', phone='01055568881', password='1111aaaa').save()
MyUser(username='pypyth22', first_name='이도연', email='python@gmail.com', phone='01077893269', password='55bb55').save()
MyUser(username='earth777', first_name='조현진', email='gigugu@daum.net', phone='01045541258', password='0123abc').save()
MyUser(username='luvy789', first_name='김서준', email='luvy789@daum.net', phone='01025879699', password='123123').save()
MyUser(username='gabba813', first_name='차하연', email='gag813@naver.com', password='515eeqe').save()
MyUser(username='bpbp4487', first_name='최건우', email='bpbp@gmail.com', phone='01077881258', password='qqw885').save()
MyUser(username='401x1127', first_name='정하은', email='401127@naver.com', password='amna88').save()
MyUser(username='victoria01', first_name='박미미', email='victoria@daum.net', password='really154').save()
MyUser(username='gaffild8', first_name='송희진', email='gaffild8@gmail.com', phone='01048897435', password='kirinkk123').save()
MyUser(username='911a112', first_name='차은우', email='9112a@naver.com', phone='01063258457', password='songsong').save()


#) Post 샘플 데이터 추가
# Post(postCode='100', category='2', author='admin', title='문의합니다', text='문의내용', published_date='2021-05-10').save()