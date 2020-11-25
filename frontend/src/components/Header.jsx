import React from 'react';
import styles from '../styles/Header.module.css'


export function Header() {
    return (
        <div className={styles.header}>
            <div className={styles.brandName}>ShareWork</div>
            <div className={styles.containerHeader}>
                <div className={styles.userName}>UserName</div>
                <div className={styles.avatar}/>
            </div>
        </div>
    );
}
