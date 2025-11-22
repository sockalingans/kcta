import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SchoolList = () => {
    const [err, setErr] = useState(null);
    const [schools, setSchools] = useState([]);
    const [newSchool, setNewSchool] = useState('');

    useEffect(() => {
        fetchSchools();
    }, []);
    
    const fetchSchools = async () => {
        try {
                const res = await axios.get('http://localhost:8000/lkup/schools/');
                setSchools(res.data);
        }
        catch (err) {
            console.log('Error fetching Schools: ', err);
            setErr('Failed to fetch data from the server');
        }
    };

    const addSchool = async () => {
        if (!newSchool) return;
        try { 
            const res = await axios.post('http://localhost:8000/lkup/schools/', {
                name: newSchool
            });
            
            setSchools([...schools, res.data]);
            setNewSchool('');
        }
        catch (err) {
            console.log('Error creating school: ', err);
            setErr('Failed to create school');
        }
    };

    const deleteSchool = async (id) => {
        try {
            await axios.delete(`http://localhost:8000/api/schools/${id}/`);
            setSchools(schools.filter((t) => t.id !== id));
        }
        catch (err) {
            console.log('Error deleting school: ', err);
            setErr('Failed to delete school');
        }
    };

    return (
        <div>
            <h1>School List</h1>

            <div>
                <input
                    name="newSchool"
                    type="text"
                    value={newSchool}
                    onChange ={(e) => setNewSchool(e.target.value)}
                    placeholder="My School..."
                />
                <button 
                    onClick={addSchool}>
                    Add School
                </button>
            </div>

            <ul>
                {schools.map((school) => (
                    <li key={school.id}>
                        <span>
                            {school.name}
                        </span>
                        <button
                            //className={styles.deleteButton}
                            onClick={() => deleteSchool(school.id)}>
                            Delete
                        </button>
                    </li>
                ))}   
            </ul>
        </div>
    );
}

export default SchoolList;