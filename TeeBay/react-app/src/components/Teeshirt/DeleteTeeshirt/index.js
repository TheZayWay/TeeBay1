import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { useModal } from "../../../context/Modal"
import { loadDeleteTeeThunk } from "../../../store/teeshirt";
import "./DeleteTeeshirt.css"

export default function DeleteTeeshirt ({props}) {
    const teeshirtId = props;
    const dispatch = useDispatch();
    const history = useHistory();
    const { closeModal } = useModal();

    const handleClick =  async (e) => {
        e.preventDefault();
        await dispatch(loadDeleteTeeThunk(teeshirtId))
            .then(() => history.push("/"))
            .then(() => closeModal())
    }

    return (
        <div className="delete-spot-modal-container">
        <div className="delete-pop-up">
            <div className="delete-header-close-button">
                {/* <span className="close-edit-button" onClick={() => closeModal()}><i className="fas fa-times"></i></span> */}
                <div className="delete-spot-header">Delete Tee</div>
            </div>
            <p className="delete-spot-text-p-tag">Are you sure you want to remove this tee?</p>
            <form className="delete-form-container" onSubmit={handleClick}>
            <button className="spot-delete-button" type="submit">Delete</button>
                <button className="spot-cancel-button" onClick={() => closeModal()}>Cancel</button>
            </form>
        </div>
    </div>
    )
}