import React from 'react';
import { Link } from 'react-router-dom';
import AuthButton from './Auth/AuthButton';
import styles from '../styles/Header.module.css';

export default function Header() {
  return (
    <div className={styles.header}>
      <Link to="/">
        <div className={styles.brandName}>ShareWork</div>
      </Link>
      <div className={styles.containerHeader}>
        <AuthButton />
        <div className={styles.avatar} />
      </div>
    </div>
  );
}
