- PSS/E

    clipboard_to_csv

sys와 clipboard만을 import해서 python만 설치된 환경에서도 가능할 것으로 예상

*주의* Clipboard를 통한 복사, 붙여넣기 방식이라 상대적으로 파일의 크기가 큰 경우에 대해서는 데이터의 손실이나 문제가 발생할 가능성이 존재

이 경우에는 PSCAD outfile(.out)을 통해 csv 파일로 변환하는 방식을 사용해야 한다.

    Merge_csv

*주의* 합치는 과정에서 후속 파일에 대해 time을 삭제하고 진행

이로 인해 plot step이 다른 csv파일에 대해서 적용하는데 제한됨

- PSCAD

    out_to_csv

ver33은 python 2.7 환경에 맞춰서 코드를 동작시켜야 함.

ver35는 python 3 환경에 맞춰서 코드를 동작시켜야 함.

단, python 3.7인 경우

sys.path.append(r"C:\Program Files\PTI\PSSE35\35.2\PSSPY37")

os.environ['PATH'] = (r"C:\Program Files\PTI\PSSE35\35.2\PSSPY37;" + os.environ['PATH'])

python 3.8인 경우

sys.path.append(r"C:\Program Files\PTI\PSSE35\35.2\PSSPY38")

os.environ['PATH'] = (r"C:\Program Files\PTI\PSSE35\35.2\PSSPY38;" + os.environ['PATH'])

이렇게 변경 후 진행해야 함.

*주의* 상위 버전의 out  파일에 대해 하위버전에서도 load 및 csv 파일을 생성하는 것을 확인

*주의* 일부로 encoding을 ver33에 대해서 CP949 / ver35에 대해서 UTF-8을 적용함. 

만일 한글이 깨져서 보인다면 실행파일을 변경해서 진행하면 개선될 것
