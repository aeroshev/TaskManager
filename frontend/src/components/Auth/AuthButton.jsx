import React from 'react';
import { useHistory } from 'react-router-dom';
import { useAuth } from './Context';
import styles from '../../styles/AuthButton.module.css';

export default function AuthButton() {
  const history = useHistory();
  const auth = useAuth();

  return auth.user ? (
    <p className={styles.hello}>
      {auth.user}
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
    <p className={styles.hello}>You are not logged in.</p>
  );
}
