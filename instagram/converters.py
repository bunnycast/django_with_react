
# 정규표현식 커스텀 컨버터 구성 (20으로 시작하는 4자리 숫자)
class YearConverter:
    regex = r"20\d{2}"

    # url에서 추출한 문자열을 뷰에 넘겨주기 전에 변환
    def to_python(self, value):
        return int(value)

    # url reverse시에 호출
    def to_url(self, value):
        return str(value)


class MonthConverter:
    regex = r"\d{1, 2}"


class DayConverter:
    regex = r"[0123]\d"
