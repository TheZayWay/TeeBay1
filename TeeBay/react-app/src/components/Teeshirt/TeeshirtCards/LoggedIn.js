import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { loadAllTeesThunk } from '../../../store/teeshirt';
import { Link } from 'react-router-dom';
import CreateTeeshirtForm from '../../Forms/SellingForm';
import { logout } from "../../../store/session";
// import './TeeshirtCards.css'


export default function LoggedIn() {
    const dispatch = useDispatch();
    const teeshirts = useSelector((state => state));
    const tees = teeshirts.tees.allTees;
    const user = teeshirts.session;
    const teesArr = Object.values(tees);

    useEffect(() => {
        dispatch(loadAllTeesThunk());
    }, [dispatch])

    const handleLogout = (e) => {
        e.preventDefault();
        dispatch(logout());
      };

    return (
        <>
        <button onClick={handleLogout}>Log Out</button>
        <p>logged in</p>
        <Link to="/selling">Sell</Link>
        <Link to="/listings">Your Account</Link>
        <hr></hr>
        <div className='card-container'>         
            {teesArr.map((teeshirt) => {
                    return (
                        <div className='card' key={teeshirt.id}>
                            <Link to={`/teeshirts/${teeshirt.id}`}>
                                <img src={teeshirt.image_url} alt='Teeshirt Preview' className='front-page-images'/>
                                <button>Buy Tee</button>
                            </Link>                           
                        </div>
                    )
                }                 
            )}
        </div>
        </>
    )
}