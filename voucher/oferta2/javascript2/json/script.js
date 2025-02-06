const API_URL = 'http://127.0.0.1:5500/voucher/oferta2/javascript2/json/';
const DEV = true;

const endPoints = {
    dados: 'dados',
};

/**
 * @typedef {'dados'} endPointsType
 */

const useApi = async (path) => {
    DEV && console.log(API_URL + path);

    try {
        const response = await fetch(`${API_URL}/${path}`);
        const jsonResponse = await response.json();

        if (response.ok) {
            return jsonResponse;
        } else {
            throw new Error(jsonResponse.message || 'Something went wrong');
        }
    } catch (err) {
        console.error(err);
        return { message:'Não foi possível se conectar com o servidor, tente novamente'}
    }
};

useApi('dados.json').then(data => console.log(data))