import { useParams, Link } from 'react-router-dom';
import { useEffect } from 'react';
import { loadTeeByIdThunk } from '../../../store/teeshirt';
import { useDispatch, useSelector } from 'react-redux';
import UpdateListingForm from '../../Forms/UpdateListing';

export default function TeeshirtDetails() {
    const dispatch = useDispatch();
    const params = useParams();
    const teeshirtId = Number(params.teeshirtId);
    const teeshirtObj = useSelector((state) => state.tees.allTees);
    const user = useSelector((state) => state.session.user)
    const teeshirt = teeshirtObj[teeshirtId]
    
    useEffect(() => {
        dispatch(loadTeeByIdThunk(teeshirtId));
    }, [dispatch]);

  return (
    <>
        <h1>Individual Teeshirt</h1>
        <img src={teeshirt?.image_url} />
        {user !== null ? <Link to="/"><button>Buy tee</button></Link> : ""}
    </>
  )
}

