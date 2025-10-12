function main(){
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

    function addContact(){
        let uName = window.prompt("Type your name!");
        let uPhone = window.prompt("Type your phone!");
        let uEmail = window.prompt("Type your email!");
        console.log(confirm('opa'))

        return {
            name: uName,
            phone: uPhone,
            email: uEmail
        }
    }

    contacts.push(addContact())
    console.log(contacts[0])
    console.log(contacts[contacts.length - 1]) 
}

main()