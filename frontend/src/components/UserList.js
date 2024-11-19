import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await axios.get('/api/users/');
        setUsers(response.data);
      } catch (error) {
        console.error("Error al cargar usuarios:", error);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div className="container">
      <h2>Lista de Usuarios</h2>
      <table className="table">
        <thead>
          <tr>
            <th>Correo</th>
            <th>Nombre</th>
            <th>Identificación</th>
            <th>Rol</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.correo}</td>
              <td>{user.nombre}</td>
              <td>{user.identification}</td>
              <td>{user.rol}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UserList;
