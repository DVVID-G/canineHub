import React, { useState } from 'react';
import axios from 'axios';

const RoleForm = () => {
  const [roleData, setRoleData] = useState({
    name: '',
    description: ''
  });

  const handleInputChange = (e) => {
    setRoleData({
      ...roleData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/roles/', roleData);
      console.log("Rol creado:", response.data);
    } catch (error) {
      console.error("Error al crear rol:", error);
    }
  };

  return (
    <div className="container">
      <h2>Crear Rol</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Nombre del Rol:</label>
          <input
            type="text"
            name="name"
            value={roleData.name}
            onChange={handleInputChange}
            className="form-control"
            required
          />
        </div>
        <div className="form-group">
          <label>Descripción:</label>
          <input
            type="text"
            name="description"
            value={roleData.description}
            onChange={handleInputChange}
            className="form-control"
          />
        </div>
        <button type="submit" className="btn btn-primary mt-3">Crear Rol</button>
      </form>
    </div>
  );
};

export default RoleForm;
