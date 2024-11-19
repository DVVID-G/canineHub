import React, { useEffect, useState } from 'react';
import { getAllUsers } from './api/usersApi';  // Asegúrate de tener la ruta correcta

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      const usersData = await getAllUsers();
      setUsers(usersData);
    };

    fetchUsers();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Lista de Usuarios</h1>
        <ul>
          {users.map(user => (
            <li key={user.id}>{user.nombre} - {user.correo}</li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;

