import React from 'react';
import Header from '../Header';
import CardList from './CardList';
import Footer from '../Footer';
import styles from '../../styles/Home.module.css';

export default function Home() {
  return (
    <div>
      <Header />
      <div className={styles.projectName}>Hello, world!</div>
      <CardList />
      <Footer />
    </div>
  );
}
