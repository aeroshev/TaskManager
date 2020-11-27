import React from 'react';
import Card from './Card';
import styles from '../../styles/CardList.module.css';

export default function CardList() {
  const list = [];
  for (let i = 0; i < 20; i += 1) {
    list.push(<Card />);
  }
  return (
    <div className={styles.cardContainer}>
      {list}
    </div>
  );
}
