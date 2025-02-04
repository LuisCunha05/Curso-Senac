const API_URL = 'https://pokeapi.co/api/v2/';
const DEV = true;
const endPoints = {
    pokemon: 'pokemon',
    type: 'type',
    stat: 'stat',
};

/**
 * @typedef {'pokemon' | 'type' | 'stat'} endPoints
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
        return { message:'Não foi possível se conectar com o servidor, tente novamente' }
    }
};

const usePokemonApi = async (nameOrId) => {

    const pokemonData = await useApi(`${endPoints.pokemon}/${nameOrId ?? ''}`);
    DEV && console.log(pokemonData);

    /**
     * Returns the ID from the complete API url and endPoint
     * @param {string} value
     * @param {endPoints} endPoint
     * @returns {number}
     */
    const getID = ( value, endPoint, ) => {
        return parseInt(value.replace(`${API_URL}${endPoint}/`, '').replace('/', ''));
    }

    const useStats = pokemonData.stats.map(item => {
        const {base_stat, stat:{ name, url }} = item
        return {name: name, value: base_stat, id: getID(url, 'stat')};
    })

    const useSprites = {default: pokemonData.sprites.front_default, shiny: pokemonData.sprites.front_shiny }

    const useTypes = pokemonData.types.map(item => {
        const {type: {name, url}} = item
        return {name: name, id: getID(url, 'type')};
    })

    return { useStats, useSprites, useTypes };
};

// Usage
(async () => {
    const { useStats, useSprites, useTypes } = await usePokemonApi(3);
    console.log(useStats);
    // console.log(useSprites);
    console.log(useTypes);
})();