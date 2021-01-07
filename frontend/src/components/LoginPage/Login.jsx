import React from 'react';
import PropTypes from 'prop-types';
import { useHistory, useLocation } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { useAuth } from '../Auth/Context';
import styles from '../../styles/Login.module.css';

export default function Login(props) {
  // eslint-disable-next-line no-unused-vars
  const { url, handler } = props;
  const history = useHistory();
  const location = useLocation();
  const auth = useAuth();
  const {
    register,
    handleSubmit,
  } = useForm();
  const { from } = location.state || { from: { pathname: '/home/' } };
  const login = () => {
    auth.signin(() => {
      history.replace(from);
    });
  };
  return (
    <form onSubmit={handleSubmit(login)}>
      <input name="username" type="text" placeholder="username" ref={register} />
      <input name="password" type="password" placeholder="password" ref={register} />
      <input name="Login" type="submit" value="Login" />
      <div className={styles.register}>
        <p className={styles.message}>
          Not registered?
        </p>
        <p className={styles.message}>
          <input name="registration" type="text" value="Sign In" onClick={() => { handler(true); }} />
        </p>
      </div>
      <div className={styles.line}>
        <hr className={styles.bar} />
        <span className={styles.text}>Or</span>
        <hr className={styles.bar} />
      </div>
      <div className={styles.method}>
        <div className={styles.item}>
          Sign in with Google
        </div>
        <div className={styles.item}>
          Sign in with Facebook
        </div>
        <div className={styles.item}>
          Sign in with VK
        </div>
      </div>
    </form>
  );
}

Login.propTypes = {
  url: PropTypes.string.isRequired,
  handler: PropTypes.func.isRequired,
};
