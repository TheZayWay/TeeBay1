import { useParams, Link, useHistory } from 'react-router-dom';
import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { loadAllUserTeesThunk } from '../../../store/teeshirt';
import DeleteTeeshirt from '../DeleteTeeshirt'

export default function SellerTeeshirts () {
    const dispatch = useDispatch();
    const history = useHistory();
    const state = useSelector((state) => state)
    const user = state.session.user;
    const userId = user.id;
    const teeshirts = state.tees.userTees;
    const teeshirtsArr = Object.values(teeshirts)
    
    

    useEffect(() => {
        dispatch(loadAllUserTeesThunk())
    }, [dispatch])


    return (
        <div>
            {teeshirtsArr.map((teeshirt) => {
                return (
                    <>
                    <img src={teeshirt.image_url} alt='Teeshirt Preview' />
                    <Link to={`/teeshirts/${teeshirt.id}/update`}>Update Listing</Link>
                    <DeleteTeeshirt props={teeshirt.id}/>
                    </>
                )
            })}
        </div>

    ) 
}