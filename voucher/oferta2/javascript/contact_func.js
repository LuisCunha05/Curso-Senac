function start(){
    let contacts = [{
        name: "Maxwell Wright",
        phone: "(0191) 719 6495",
        email: "Curabitur.egestas.nunc@nonummyac.co.uk"
    }, {
        name: "Raja Villarreal",
        phone: "0866 398 2895",
        email: "posuere.vulputate@sed.com"
    }, {
        name: "Helen Richards",
        phone: "0800 1111",
        email: "libero@convallis.edu"
    }];

    //{name: String, phone: String, email: String}[]
    /**
     * Show the contents of object in the array
     * @param {Array.<{name: String, phone: String, email: String}>} array 
     * @param {number} index 
     */
    const showContact = (array, index) => {
        if(!(array instanceof Array)){
            alert('Parametro não é do tipo Array')
            return
        }
        console.log(`Name: ${array[index].name}, Phone: ${array[index].phone}, E-mail: ${array[index].email}`)
    }

    /**
     * 
     * @param {Array.<{name: String, phone: String, email: String}>} array 
     */
    const showAllContacts = array => {
        if(!(array instanceof Array)){
            alert('Parametro não é do tipo Array')
            return
        }

        for(let index = 0; index < array.length; index++){
            console.log(`Contato ${index}:`)
            showContact(array, index)
        }
    }

    /**
     * Adds a new object in the array
     * @param {Array.<{name: String, phone: String, email: String}>} arr 
     * @param {String} nName 
     * @param {String} nPhone 
     * @param {String} nEmail 
     */
    const addContact = (arr, nName, nPhone, nEmail) => {
        if(!(arr instanceof Array)){
            alert('Parametro não é do tipo Array')
            return
        }
        if(typeof nName != 'string' || typeof nPhone != 'string' || typeof nEmail != 'string'){
            alert('Parametro não é do tipo String')
            return
        }

        arr.push({
            name: nName,
            phone: nPhone,
            email: nEmail
        })
    }

    showAllContacts(contacts)
}
start()