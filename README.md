# scrapyserver
공공데이터 crawler 개발을 위한 python코드 repo

*하나의 폴더에 두번째 깊이에 스크래피 startproject만들어서 실행 및 관리 가능


---
<!-- Checklist Start -->

## 작업 Checklist
QA작업은 기능작동확인 위주라, 기능작동에는 영향은 없지만 "생산성이나 안전성, 각종 상황에서의 대응능력 등"
에 꼭 필요한 작업사항은, 각 repo별 별도 Checklist를 만들어서 관리한다

### 작업환경-배포환경별 Checklist: 공통
| title                      	                                                                 | development | staging      | production                   | etc  |
| :---                                                                                           | :---:       | :----:       | :---:                        | :---: |
| 해당 프로젝트는 실행배포환경별 어떤Tool-어느위치에 배포실행관리가 되는가?(이용시스템-머신종류,실행OS등)| 개발자 pc   |         	  | 회사내부서버(ubuntu 18.04LTS) 파이썬환경 |       |
| 실행배포환경별 [logging, Crashlytics]등 로깅시스템 셋팅여부 및 종류	                           |              |         	 |                              |       |
| 기본 - 빌드실행시 [각종 환경변수, 설정파일]이 실행배포환경에 맞게 자동변경 되는가?                  |           	  |         	|                              |       |
| logging - 빌드실행시 [각종 환경변수, 설정파일]이 실행배포환경에 맞게 자동변경 되는가?              |             	  |         	|                              |       |
| logging - 실행배포환경별 어떤Tool-어느위치에 (장애발생)log메시지가 저장 및 report되는가?            |             |         	    |                             |       |

### 작업환경-배포환경별 Checklist: 이용조건별[개발언어, 프로젝트type, 프레임워크, 이용Tool]
| title                      	                                                              | development | staging      | production | etc  |
| :---                                                                                        | :---:            | :----:         | :---:          | :---: |
| firebase - 빌드실행시 [각종 환경변수, 설정파일]이 실행배포환경에 맞게 자동변경 되는가?               |             	  |         	    |               |       |
| scrapy - 빌드실행시 [각종 환경변수, 설정파일]이 실행배포환경에 맞게 자동변경 되는가?             |             	  |         	    |               |       |
| mongodb - 빌드실행시 [각종 환경변수, 설정파일]이 실행배포환경에 맞게 자동변경 되는가?             |             	  |         	    |               |       |
| API endpoint - 빌드실행시 [각종 환경변수, 설정파일]이 실행배포환경에 맞게 자동변경 되는가?        |           	  |         	    |               |       |


### 문장형 Checklist: 공통
- [ ] 각 언어-프레임워크-Tool별 Coding-Variable convention을 준수 하였는가?
- [ ] [개발이용언어, 프로젝트type, 프레임워크, 이용Tool]등 에서 권장하는 디렉토리-파일-파일명 structure 패턴을 준수 하였는가?
- [ ] 고유기능 구현시, 인터페이스-function 등으로 wrap 후 구현-이용 하였는가?
    * 라이브러리, custom로직을 감싸지 않고 그냥 막쓰면, 한 파일당 code라인수가 너무 길어져 복잡져서 나중에 수정이 어려우며, function별 기능단위테스트시에 분할이 어려움
    * 특정 라이브러리의 호환사용성에 문제가 생기거나, 서버위치 실행위치별 전략적 서비스 기능실행배포가 필요한 경우,
     기타 이유등으로 해당기능의 라이브러리를 변경하는등 기능(내부)로직변경시, 원활하고 신속한 기능수정을 위하여
- [ ] 고유환경변수-Variable 선언사용시, 각종 env-config파일 폴더 등에서 별도로 관리되고 있는가?
- [ ] logging환경관련: production환경에서 error이상의 장애발생log메시지 발생시, <br /> **현재 production 배포환경에서, 어느위치로 실시간 report확인이 가능하도록 설정되어 있는가?**
    - [ ] report 이메일
    - [ ] cloud console 모바일 app(gcp, aws등)
    - [ ] slack등 운영모니터링 전용 app
    - [ ] 셋팅된 production logging 환경을 추가작성하기

- [ ] "vscode등 개발IDE 개발Tool" 등을 이용한 [debug-breakpoint, extension tool] 환경을 [구축하는 방법-문서내용, 또는 설정파일(.vscode 등)]로 저장하였는가?
- [ ] 문법코드분석정리 linter 적절셋팅 완료여부
    * python: black + @
    * ts: typescript-eslint + prettier + @
- [ ] 언어-국가옵션 변경시 영향을 받는 변수의, i18n 적절셋팅 완료여부
- [x] .editorconfig 적절셋팅 완료여부
- [ ] .gitignore 적절셋팅 완료여부
- [ ] 미디어 resources 파일의 과도한 사용, 또는 필요이상의 고용량 파일이 사용되지 않도록 검수수정 하였는가?
- [ ] production 빌드된 패키지의 용량이 배포플랫폼에 적절한 용량인가?
    * [log, tmp, 미사용 파일-라이브러리, 각종docs문서-미디어파일]등 실행패키지 필요없는 파일이 빌드시 제외되었는가?
    * android기준: 100MB 이하(유사카테고리 다른 app과 비교했을때 기준, 60MB이내가 적절해보임)
- [ ] readme.md에 [작업시 알거나 확인해야하는 내용, Checklist] 등의 안내내용 작성완료여부?

### 문장형 Checklist: 이용조건별[개발언어, 프로젝트type, 프레임워크, 이용Tool]
- [ ] 빌드실행설정 적절셋팅 완료여부
    - [ ] JS_TS: tsconfig.json 적절셋팅 완료여부
    - [ ] JS_TS: package.json 필요실행내용별 run script 셋팅완료여부(프로젝트 각 빌드단계별 실행 명령어를 모르는 사람도, npm run script로 실행이 가능한가?)
    - [ ] JS_TS: package.json 필요실행 라이브러리 이름-버전명을, dependencies, devDependencies 에 올바르게 작성하였는가?

<!-- Checklist End -->



[전주시청] - jeonjuevent - 전주시 공지사항 및 새소식 데이터 수집

-셀레늄, 스크래피 제작

-사용안함


[보조금24] - sub24 - 보조금24 사이트 서비스 데이터 수집

-셀레늄 제작 (sub24.py)
-명령어
    python sub24.py

-동작과정
    보조금24 서비스 전체 수집 -> 수집한 데이터 DB저장 -> 시트 입력

-참고사항
    각 서비스 상세페이지 구조가 조금씩 다르니, 새로 작성되는 서비스 구조에 따라 실행시 에러 뜰 수 있음. 그럴때마다 if문 추가 필요.

-sub24_puls
-서비스분야,생애주기,소득분위,특성 카테고리 추가 데이터 수집



[복지로] -welfare - 복지로 사이트 서비스 데이터 수집

-셀레늄 제작 (welfare.py)
-명령어
    python welfare.py

-동작과정
    복지로 지자체 서비스 전체 수집 -> 시트 입력

-참고사항
    next 버튼으로 최대 100개 까지 설정, 데이터가 많아지면 추가 수정 필요(첫번째 for문 range)


[정부24] -gov24 - 정부24 데이터 수집

-open API 활용 (gov24.py)
-명령어
    python gov24.py

-동작과정
    svcId 기준 데이터 가져와서 시트에 삽입

-참고사항
    개발 일일 트래픽 제한 1000


## 참고사항
- https://github.com/naming-convention/naming-convention-guides/tree/master/python
