import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PersonList = () => {
    const [err, setErr] = useState(null);
    const [persons, setPersons] = useState([]);
    
    useEffect(() => {
        fetchPersons();
    }, []);  

    const fetchPersons = async () => {
        try {
                const res = await axios.get('http://localhost:8000/prsn/persons/');
                setPersons(res.data);
        }
        catch (err) {
            console.log('Error fetching Persons: ', err);
            setErr('Failed to fetch data from the server');
        }
    };

    return (
        <div>
            <h1>Person List</h1>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Full Name</th>
                        <th>Email</th>
                        <th>Age</th>
                    </tr>
                </thead>
                <tbody>
                    {persons.map((person) => (
                        <tr key={person.id}>
                            <td>{person.id}</td>
                            <td>{person.fullname}</td>
                            <td>{person.email}</td>
                            <td>{person.age}</td>
                        </tr> 
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default PersonList;