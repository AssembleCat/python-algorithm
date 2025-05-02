"""
좋은 패스워드를 만드는것은 어려운 일이다.
 대부분의 사용자들은 buddy처럼 발음하기 좋고 기억하기 쉬운 패스워드를 원하나,
 이런 패스워드들은 보안의 문제가 발생한다.
 어떤 사이트들은 xvtpzyo 같은 비밀번호를 무작위로 부여해 주기도 하지만, 사
 용자들은 이를 외우는데 어려움을 느끼고 심지어는 포스트잇에 적어 컴퓨터에 붙여놓는다.
 가장 이상적인 해결법은 '발음이 가능한' 패스워드를 만드는 것으로 적당히 외우기 쉬우면서도 안전하게 계정을 지킬 수 있다.

회사 FnordCom은 그런 패스워드 생성기를 만들려고 계획중이다.
당신은 그 회사 품질 관리 부서의 직원으로 생성기를 테스트해보고 생성되는 패스워드의 품질을 평가하여야 한다.
높은 품질을 가진 비밀번호의 조건은 다음과 같다.

모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
이 규칙은 완벽하지 않다;우리에게 친숙하거나 발음이 쉬운 단어 중에서도 품질이 낮게 평가되는 경우가 많이 있다.

TODO(any, all 같은 iterable한 객체를 검사하는 함수를 사용하면 가독성이 높다)
TODO(리스트 컴프리헨션을 유연하게 사용하자. [c in m for c in password])
"""

m = ['a', 'e', 'i', 'o', 'u']
while True:
    password = input()
    if password == 'end':
        break

    # 조건 1: 모음 포함 여부
    step1 = any(c in m for c in password)

    # 조건 2: 모음 3개 or 자음 3개 연속 금지
    step2 = True
    digit_types = [c in m for c in password]
    count = 1
    for i in range(1, len(password)):
        if digit_types[i] == digit_types[i - 1]:
            count += 1
            if count >= 3:
                step2 = False
                break
        else:
            count = 1

    # 조건 3: 같은 문자 연속 (ee, oo는 허용)
    step3 = True
    for i in range(1, len(password)):
        if password[i] == password[i - 1] and password[i] not in ['e', 'o']:
            step3 = False
            break

    if step1 and step2 and step3:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
