import axios from 'axios';

// Asegúrate que esta URL sea la correcta, según tu configuración de Django
const BASE_URL = 'http://localhost:8000/api/';

const userApi = () => axios.create({
    baseURL: BASE_URL,
});

// Obtener todos los usuarios
export const getAllUsers = async () => {
    try {
        const response = await userApi().get('users/');  // Aquí usamos 'users/' en plural
        return response.data;
    } catch (error) {
        console.error('Error al obtener todos los usuarios:', error);
        return [];
    }
}

// Crear un nuevo usuario
export const createUser = async (user) => {
    try {
        const response = await userApi().post('users/', user);  // 'users/' en plural
        return response.data;
    } catch (error) {
        console.error('Error al crear un usuario:', error);
        return null;
    }
}

// Actualizar un usuario existente
export const updateUser = async (user) => {
    try {
        const response = await userApi().put(`users/${user.id}/`, user);  // 'users/' en plural
        return response.data;
    } catch (error) {
        console.error('Error al actualizar el usuario:', error);
        return null;
    }
}

// Eliminar un usuario
export const deleteUser = async (id) => {
    try {
        const response = await userApi().delete(`users/${id}/`);  // 'users/' en plural
        return response.data;
    } catch (error) {
        console.error('Error al eliminar el usuario:', error);
        return null;
    }
}

// Obtener un usuario específico
export const getUser = async (id) => {
    try {
        const response = await userApi().get(`users/${id}/`);  // 'users/' en plural
        return response.data;
    } catch (error) {
        console.error('Error al obtener el usuario:', error);
        return null;
    }
}




