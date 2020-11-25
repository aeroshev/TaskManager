import React from 'react';
import { Header } from '../Header'
import { CardList } from './CardList';
import styles from '../../styles/Home.module.css'


export function Home() {
    return (
        <div>
            <Header/>
            <div className={styles.projectName}>Hello, world!</div>
            <CardList/>
        </div>
    );
}
