import React from 'react';
import PropTypes from 'prop-types';
import { useHistory, useLocation } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { useAuth } from '../Auth/Context';
import styles from '../../styles/Login.module.css';
import google from '../../icons/google.png';
import facebook from '../../icons/facebook.png';
import vk from '../../icons/vk.png';

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
        {/* eslint-disable-next-line react/button-has-type */}
        <button className={styles.message} onClick={() => { handler(true); }}>
          Sign In
        </button>
      </div>
      <div className={styles.line}>
        <hr className={styles.bar} />
        <span className={styles.text}>Or</span>
        <hr className={styles.bar} />
      </div>
      <div className={styles.method}>
        <div className={styles.item}>
          <div className={styles.container}>
            <img src={google} width="30px" height="30px" alt="google icon" />
            <p>Sign in with Google</p>
          </div>
        </div>
        <div className={styles.item}>
          <div className={styles.container}>
            <img src={facebook} width="30px" height="30px" alt="facebook icon" />
            <p>Sign in with Facebook</p>
          </div>
        </div>
        <div className={styles.item}>
          <div className={styles.container}>
            <img src={vk} width="30px" height="30px" alt="vk icon" />
            <p>Sign in with VK</p>
          </div>
        </div>
      </div>
    </form>
  );
}

Login.propTypes = {
  url: PropTypes.string.isRequired,
  handler: PropTypes.func.isRequired,
};
