# AskDjango Day6 오프라인 강의 복습

## 강의

날짜: 2017.07.23(일) 13:00 ~ 17:00

장소: [쎄임페이지](http://map.naver.com/?mapmode=0&lng=076353085b95ed69bca3d6e40f6722da&pinId=35751344&lat=de07418b623af3b514feca9c5cf61c60&dlevel=11&enc=b64&pinType=site)

## 수업 내용

### 장고 Form/ModelForm

장고를 쓰는 데 Form을 모르고 계신다면, 장고를 쓰고 계신 것이 아닙니다. Form을 공부하고 공부하세요. 사용자에게 스마트한 입력방법을 제공해주며, 사용자로부터의 입력을 효과적으로 체크할 수 있습니다. 코드 몇 줄이면 됩니다.

### 유효성 검사

유저로부터의 입력은 절대 신뢰해서는 안됩니다. 휴대폰 번호를 입력하라고 해서 모든 유저가 010-1234-1234 패턴을 입력하지 않습니다. “01a-123z-1234”라고 입력하는 유저가 있습니다. 장고에서 지원하는 유효성 검사 기능을 통해 물샐틈없이 유저로부터의 입력값을 체크할 수 있습니다. 장고를 믿고, 이해해보세요.

### Form을 보다 멋지게 만들기

폼도 이뻐고 멋져야 쓸 맛이 납니다. 폼을 좀 더 깔끔하게 다듬는 방법에 대해서 살펴보겠습니다.

## 테스트 환경

| 항목 | 내용 |
| :--: | :--: |
| Django | v1.11.3 |
| Python | v3.5 |
| Django-debug-toolbar | v1.8 |

### 사용 방법

```
# git clone https://github.com/westporch/askdjango-day06-review.git
# cd YOUR_PATH/askdjango-day06-review/myenv/bin
# source activate
(myenv) # 
```
