import React from 'react';
import { Link } from 'react-router-dom';
import styles from '../../styles/Login.module.css';

export default function Login() {
  return (
    <div className={styles.loginPage}>
      <div className={styles.form}>
        <form>
          <input type="text" placeholder="username" />
          <input type="password" placeholder="password" />
          <Link to="/">
            <button type="button">login</button>
          </Link>
          <p className="message">
            Not registered?
          </p>
        </form>
      </div>
    </div>
  );
}
