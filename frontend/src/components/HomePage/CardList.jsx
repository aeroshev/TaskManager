import React from 'react';
import PropTypes from 'prop-types';
import Card from './Card';
import styles from '../../styles/CardList.module.css';

export default function CardList(props) {
  const { projectsList } = props;
  const list = [];
  projectsList.forEach((item) => {
    const project = <Card key={item.id} content={item} />;
    list.push(project);
  });
  return (
    <div className={styles.cardContainer}>
      {list}
    </div>
  );
}

CardList.defaultProps = {
  projectsList: [],
};

CardList.propTypes = {
  projectsList: PropTypes.arrayOf(PropTypes.objectOf(PropTypes.string)),
};
