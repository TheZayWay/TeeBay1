import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { loadAllTeesThunk } from '../../../store/teeshirt';
import { Link } from 'react-router-dom';
import './TeeshirtCards.css'
import LoggedOut from './LoggedOut';
import LoggedIn from './LoggedIn';

export default function TeeshirtCards() {
    const teeshirts = useSelector((state => state));
    const user = teeshirts.session.user;

    return (
        <>
            {user === null ? <LoggedOut /> : <LoggedIn />}      
        </>
    )
}

