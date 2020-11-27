import React, { useState, useEffect } from 'react';
import Header from '../Header';
import CardList from './CardList';
import Footer from '../Footer';
import styles from '../../styles/Home.module.css';

export default function Home() {
  const API_URL = 'https://localhost/api/';
  const [projectsList, setProjectsList] = useState([]);
  async function getProjects() {
    try {
      const response = await fetch(`${API_URL}/projects/`, {
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
