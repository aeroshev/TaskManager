import React from 'react';
import { HeaderHome } from './HeaderHome'
import { CardList } from './CardList';
import styles from '../../styles/Home.module.css'


export function Home() {
    return (
        <div>
            <HeaderHome/>
            <div className={styles.projectName}>Hello, world!</div>
            <CardList/>
        </div>
    );
}
