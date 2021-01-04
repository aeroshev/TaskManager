import React from 'react';
import PropTypes from 'prop-types';
import { useForm } from 'react-hook-form';
import styles from '../../styles/Login.module.css';

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export default function Login(props) {
  // eslint-disable-next-line no-unused-vars
  const { url, handler } = props;
  const {
    register,
    handleSubmit,
  } = useForm();
  const onLogin = async (data) => {
    await sleep(2000);
    if (data.username === 'bill') {
      alert(JSON.stringify(data));
    } else {
      alert('There is an error');
    }
  };
  return (
    <form onSubmit={handleSubmit(onLogin)}>
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
