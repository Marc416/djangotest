from django.contrib.auth.forms import UserCreationForm

# 기존의 어카운트 만들던 폼을 상속한다.
class AccountUpdateForm(UserCreationForm):
    # 생성자를 만든다.
    def __init__(self, *args, **kwargs):
        # 상속한 부모의 생성자를 실행한다.
        super().__init__(*args, **kwargs)
        # 유저 아이디를 바꾸는 것을 금지한다.
        self.fields['username'].disabled = True