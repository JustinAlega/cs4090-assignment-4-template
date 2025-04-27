from hypothesis import given
import hypothesis.strategies as st
from my_module import login_user, reset_password, update_user_profile


@given(username=st.text(min_size=1), password=st.text(min_size=1))
def test_login_user_random(username, password):
    result = login_user(username, password)
    assert result in [True, False]

@given(username=st.text(min_size=1), new_password=st.text(min_size=1))
def test_reset_password_random(username, new_password):
    result = reset_password(username, new_password)
    assert isinstance(result, str)

@given(username=st.text(min_size=1), profile_info=st.dictionaries(st.text(), st.text()))
def test_update_profile_random(username, profile_info):
    result = update_user_profile(username, profile_info)
    assert isinstance(result, str)

@given(username=st.text(min_size=1))
def test_reset_password_empty(username):
    result = reset_password(username, "")
    assert isinstance(result, str)

@given(profile_info=st.dictionaries(st.text(), st.text()))
def test_update_profile_no_username(profile_info):
    result = update_user_profile("", profile_info)
    assert isinstance(result, str)
