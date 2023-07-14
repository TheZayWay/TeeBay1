import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { loadAllTeesThunk } from '../../../store/teeshirt';
import { Link } from 'react-router-dom';
import './TeeshirtCards.css'

export default function LoggedOut() {
    const dispatch = useDispatch();
    const teeshirts = useSelector((state => state));
    const tees = teeshirts.tees.allTees;
    const user = teeshirts.session;
    const teesArr = Object.values(tees)

    useEffect(() => {
        dispatch(loadAllTeesThunk());
    }, [dispatch])

    return (
        <>
        <p>Hi(<Link to='/login'>Sign in</Link>)</p>
        <div className='card-container'>
            <div>logged out</div>
            {teesArr.map((teeshirt) => {
                    return (
                        <div className='card' key={teeshirt.id}>
                            <Link to={`/teeshirts/${teeshirt.id}`}>
                                <img src={teeshirt.image_url} alt='Teeshirt Preview' className='front-page-images'/>
                            </Link>
                            <div>
                                <div>
                                    <div>

                                    </div>
                                    <div>
                                        <span></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )
                }                 
            )}
        </div>
        </>
    )
}