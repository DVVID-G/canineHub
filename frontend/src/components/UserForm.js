import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserForm = () => {
  const [roles, setRoles] = useState([]);
  const [formData, setFormData] = useState({
    correo: '',
    nombre: '',
    rol: '',
    identification: '',
    permission: ''
  });

  // Cargar roles desde la API
  useEffect(() => {
    const fetchRoles = async () => {
      try {
        const response = await axios.get('/api/roles/');
        setRoles(response.data);
      } catch (error) {
        console.error("Error al cargar los roles", error);
      }
    };

    fetchRoles();
  }, []);

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/users/', formData);
      console.log("Usuario creado:", response.data);
    } catch (error) {
      console.error("Error al crear el usuario:", error);
    }
  };

  return (
    <div className="container">
      <h2>Crear Usuario</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Correo:</label>
          <input
            type="email"
            name="correo"
            value={formData.correo}
            onChange={handleInputChange}
            className="form-control"
            required
          />
        </div>
        <div className="form-group">
          <label>Nombre:</label>
          <input
            type="text"
            name="nombre"
            value={formData.nombre}
            onChange={handleInputChange}
            className="form-control"
            required
          />
        </div>
        <div className="form-group">
          <label>Identificación:</label>
          <input
            type="text"
            name="identification"
            value={formData.identification}
            onChange={handleInputChange}
            className="form-control"
            required
          />
        </div>
        <div className="form-group">
          <label>Permission:</label>
          <input
            type="text"
            name="permission"
            value={formData.permission}
            onChange={handleInputChange}
            className="form-control"
          />
        </div>
        <div className="form-group">
          <label>Rol:</label>
          <select name="rol" value={formData.rol} onChange={handleInputChange} className="form-control">
            <option value="">Seleccione un rol</option>
            {roles.map((rol) => (
              <option key={rol.id} value={rol.name}>
                {rol.name}
              </option>
            ))}
          </select>
        </div>
        <button type="submit" className="btn btn-primary mt-3">Crear Usuario</button>
      </form>
    </div>
  );
};

export default UserForm;
