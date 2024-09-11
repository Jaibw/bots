import streamlit as st
from streamlit_rsa_auth_ui import SignoutEvent
from streamlit_ldap_authenticator import Authenticate, UserInfos

from typing import Optional, Union, Literal

# Declare the authentication object
auth = Authenticate(
    st.secrets['ldap'],
    st.secrets['session_state_names'],
    st.secrets['auth_cookie']
)


def login(user: Union[UserInfos, str]) -> Optional[str]:
    st.session_state.TestSs = {"login_successful": True}


def logout(event: SignoutEvent) -> Optional[Literal['cancel']]:
    if 'TestSs' in st.session_state:
        del st.session_state.TestSs
    if 'TestSs' in st.session_state:
        return 'cancel'


# Login Process
user = auth.login(callback=login)
if user is not None:
    # st.set_page_config(initial_sidebar_state='expanded',)
    auth.createLogoutForm({'message': f"Welcome {user['displayName']}"}, callback=logout)

    # Your page application can be written below
    st.write("# Welcome to my App! ... 👋")
    st.write(user)

