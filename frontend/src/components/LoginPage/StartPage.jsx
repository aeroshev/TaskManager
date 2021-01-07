import React, { useState } from 'react';
import PropTypes from 'prop-types';
import Login from './Login';
import Register from './Register';
import styles from '../../styles/StartPage.module.css';

export default function StartPage(props) {
  const { url } = props;
  const [regPage, setRegPage] = useState(false);
  let currentFace = <Login url={url} handler={setRegPage} />;
  if (regPage) {
    currentFace = <Register url={url} />;
  }

  return (
    <div className={styles.loginPage}>
      <h1>Share Work</h1>
      <div>{currentFace}</div>
    </div>
  );
}

StartPage.propTypes = {
  url: PropTypes.string.isRequired,
};
