const GET_ALL_TEES = 'tees/getAllTees';
const GET_ALL_USER_TEES = '/tees/getAllUserTees';
const GET_TEE_BY_ID = '/tees/getTeeById';
const CREATE_TEE = '/tees/createTee';
const EDIT_TEE = '/tees/editTee';
const DELETE_TEE = '/tees/deleteTee';


const loadAllTees = (tees) => {
    return {
        type: GET_ALL_TEES,
        tees
    }
};

const loadAllUserTees = (tees) => {
    return {
        type: GET_ALL_USER_TEES,
        tees
    }
};

const loadTeeById = (tee) => {
    return {
        type: GET_TEE_BY_ID,
        tee
    }
};

const loadCreateTee = (tee) => {
    return {
        type: CREATE_TEE,
        tee
    }
};

const loadEditTee = (tee) => {
    return {
        type: EDIT_TEE,
        tee
    }
};

const loadDeleteTee = (teeId) => {
    return {
        type: DELETE_TEE,
        teeId
    }
};

export const loadAllTeesThunk = () => async (dispatch) => {
    const response = await fetch('/api/teeshirts');
    if (response.ok) {
        const teeshirts = await response.json();
        dispatch(loadAllTees(teeshirts));
        return teeshirts;
    }
};

export const loadAllUserTeesThunk = () => async (dispatch) => {
    const response = await fetch('/api/teeshirts/current')
    if (response.ok) {
        const userTeeshirts = await response.json();
        const userTeeshirtsArr = Object.values(userTeeshirts)[0];
        dispatch(loadAllUserTees(userTeeshirtsArr));
        return userTeeshirtsArr;
    }
}

export const loadTeeByIdThunk = (teeshirtsId) => async (dispatch) => {
    const response = await fetch(`/api/teeshirts/${teeshirtsId}`); 
    if (response.ok) {
        const teeshirt = await response.json();
        dispatch(loadTeeById(teeshirt));
        return teeshirt;
    }
}
export const loadCreateTeeThunk = (userId, teeshirt) => async (dispatch) => {
    const response = await fetch(`/api/teeshirts/${userId}/teeshirt/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(teeshirt)
    });

    if (response.ok) {
        const newTeeshirt = await response.json();
        console.log("ID", newTeeshirt)
        dispatch(loadCreateTee(newTeeshirt))
        return newTeeshirt
    }
}

export const loadEditTeeThunk = (teeshirtId, teeshirt) => async (dispatch) => {
    const response = await fetch(`/api/teeshirts/${teeshirtId}/update`, {
        method: 'POST', 
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(teeshirt)
    });
    console.log("res", response)
    if (response.ok) {
        const updatedTeeshirt = await response.json();
        const newlyUpdatedTeeshirt = {...updatedTeeshirt}
        dispatch(loadEditTee(newlyUpdatedTeeshirt));
        console.log(newlyUpdatedTeeshirt, "NEWNEW")
        return newlyUpdatedTeeshirt;
    }
};

export const loadDeleteTeeThunk = (teeshirtId) => async (dispatch) => {
    const response = await fetch(`/api/teeshirts/delete/${teeshirtId}`, {
        method: 'DELETE'
    });
    if (response.ok) {
        dispatch(loadDeleteTee(teeshirtId));
    }
};


const initialState = {
    allTees: {},
    userTees: {}
};

const teeshirtReducer = (state = initialState, action) => {
    switch(action.type) {
        case GET_ALL_TEES: {
            const newState = {
                allTees: {},
                userTees: {}
            };
            const actTees = action.tees.teeshirts;
            actTees.map(tee => {newState.allTees[tee.id] = tee})
            return newState;
        }
        case GET_ALL_USER_TEES: {
            const newState = {...state, userTees: {}};
            const teesArr = action.tees;
            teesArr.map(tee => {newState.userTees[tee.id] = tee})
            return newState;
        }
        case GET_TEE_BY_ID: {
            const newState = {...state};
            newState.allTees[action.tee.id] = action.tee;
            return newState;
        }
        case CREATE_TEE: {
            const newState = {...state};
            newState.allTees[action.tee.id] = action.tee;
            return newState;
        }
        case EDIT_TEE: {
            const newState = {...state}
            newState.allTees[action.tee.id] = action.tee;
            return newState;
        }
        case DELETE_TEE: {
            const newState = {...state};
            delete newState.allTees[action.teeId];
            return newState;
        }
        default: {
            return state;
        }
    }
}

export default teeshirtReducer