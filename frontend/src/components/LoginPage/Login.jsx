import React from 'react';
import { useForm } from 'react-hook-form';
import styles from '../../styles/Login.module.css';

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export default function Login() {
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
    <div className={styles.loginPage}>
      <h1>Share Work</h1>
      <form onSubmit={handleSubmit(onLogin)}>
        <input name="username" type="text" placeholder="username" ref={register} />
        <input name="password" type="password" placeholder="password" ref={register} />
        <input name="Login" type="submit" value="Login" />
        <p className="message">
          Not registered?
        </p>
      </form>
    </div>
  );
}
