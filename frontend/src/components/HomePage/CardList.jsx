import React from 'react';
import Card from './Card';
import styles from '../../styles/CardList.module.css';

export default function CardList(props) {
  // eslint-disable-next-line react/prop-types
  const { projectsList } = props;
  const list = [];

  // eslint-disable-next-line react/prop-types
  projectsList.forEach((item, idx) => {
    // eslint-disable-next-line react/no-array-index-key
    const project = <Card key={idx} content={item} />;
    list.push(project);
  });
  return (
    <div className={styles.cardContainer}>
      {list}
    </div>
  );
}
