import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";

export default function UpdateAlbum ()  { 
    const navigate = useNavigate()
    const {albumId} = useParams()

    const handleSubmit = () => { 
        navigate(`/albums/${albumId}/update`)
    }
    

  return (
    <>
      <button onClick={handleSubmit} >Update</button>
    </>
  )
}