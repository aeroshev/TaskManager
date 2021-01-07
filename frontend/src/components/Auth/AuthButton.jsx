import React from 'react';
import { useHistory } from 'react-router-dom';
import { useAuth } from './Context';

export default function AuthButton() {
  const history = useHistory();
  const auth = useAuth();

  return auth.user ? (
    <p>
      Welcome!
      {/* eslint-disable-next-line react/jsx-no-comment-textnodes */}
      {' '}
      {/* eslint-disable-next-line react/button-has-type */}
      <button
        onClick={() => {
          auth.signout(() => history.push('/login/'));
        }}
      >
        Sing out
      </button>
    </p>
  ) : (
    <p>You are not logged in.</p>
  );
}
