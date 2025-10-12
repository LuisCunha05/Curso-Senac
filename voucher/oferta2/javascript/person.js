function main(){
    class Person {
        constructor(name, phone, email) {
            this.name = name;
            this.phone = phone;
            this.email = email
        }

        printPerson() {
            console.log(`${this.name}/${this.phone}/${this.email}`)
        }
    }

    p1 = new Person( 'Maxwell Wright', '(0191) 719 6495', 'Curabitur.egestas.nunc@nonummyac.co.uk')

    p1.printPerson()
}
main()