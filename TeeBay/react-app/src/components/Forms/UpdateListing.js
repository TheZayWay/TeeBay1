import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { loadEditTeeThunk, loadTeeByIdThunk } from "../../store/teeshirt";
import './UpdateListing.css'
import { useParams } from "react-router-dom";

export default function UpdateListingForm() {
  const dispatch = useDispatch();
  const {teeshirtId} = useParams();
  const history = useHistory();
  const state = useSelector((state) => state.tees);
  console.log("state", state)
  const [name, setName] = useState();
  const [type, setType] = useState();
  const [description, setDescription] = useState();
  const [image_url, setImage_Url] = useState();
  const [brand, setBrand] = useState();
  const [errors, setErrors] = useState([]);
//   const [submitted, setSubmitted] = useState(false);

const handleSubmit = async (e) => {
      e.preventDefault();
      const teeshirt = {
        name: name,
        type:type,
        description: description,
        image_url: image_url,
        brand: brand
      }
      
      const newTeeshirt = await dispatch(loadEditTeeThunk(teeshirtId,teeshirt));
      history.push(`/teeshirts/${newTeeshirt.id}`);
  }
      
    return (
        <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          className=""
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="Type">Type:</label>
        <select
          type=""
          className=""
          value={type}
          onChange={(e) => setType(e.target.value)}
          required
        >
          <option>Short Sleeve</option> 
          <option>Long Sleeve</option>
          <option>Button Short Sleeve</option>
          <option>Button Long Sleeve</option>
          <option>Thermal</option>
          <option>Undershirt</option>
        </select>
      </div>
      <div>
        <label htmlFor="description">Description:</label>
        <textarea
          className=""
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        ></textarea>
      </div>
      <div>
        <label htmlFor="image_url">Image Url:</label>
        <input 
          type="text"
          className=""
          value={image_url}
          onChange={(e) => setImage_Url(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="image_url">Brand:</label>
        <input 
          type="text"
          className=""
          value={brand}
          onChange={(e) => setBrand(e.target.value)}
        />
      </div>
      <button type="submit">Update Listing</button>
    </form>
    )
}