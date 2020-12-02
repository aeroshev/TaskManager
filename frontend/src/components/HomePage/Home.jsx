import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Header from '../Header';
import CardList from './CardList';
import Footer from '../Footer';
import styles from '../../styles/Home.module.css';

export default function Home(props) {
  const { url } = props;
  const [projectsList, setProjectsList] = useState([]);
  async function getProjects() {
    try {
      const response = await fetch(`${url}/projects/`, {
        method: 'GET',
        mode: 'cors',
        credentials: 'include',
      });

      const jsonResponse = await response.json();
      setProjectsList(jsonResponse.response);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    getProjects();
  });
  return (
    <div>
      <Header />
      <div className={styles.projectName}>Hello, world!</div>
      <CardList projectsList={projectsList} />
      <Footer />
    </div>
  );
}

Home.propTypes = {
  url: PropTypes.string.isRequired,
};
