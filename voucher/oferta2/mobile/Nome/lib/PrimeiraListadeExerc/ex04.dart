import 'package:flutter/material.dart';
 
class BikeVendor extends StatefulWidget {
  @override
  _BikeVendorState createState() => _BikeVendorState();
}
 
class _BikeVendorState extends State<BikeVendor> {
  final TextEditingController _empregados = TextEditingController();
  final TextEditingController _salminimo = TextEditingController();
  final TextEditingController _bikepreco = TextEditingController();
  final TextEditingController _bikevendida = TextEditingController();
  String _resultado = '';
 
  void _converter() {
    final empregados = double.tryParse(_empregados.text);
    final salMin = double.tryParse(_salminimo.text);
    final bikePrice = double.tryParse(_bikepreco.text);
    final bikeVendidas = double.tryParse(_bikevendida.text);
    
    if (empregados != null && salMin != null && bikePrice != null && bikeVendidas != null) {
      var comissao = bikePrice * 0.15;
      var adicional = (bikeVendidas * comissao)/empregados;
      var ganho = bikeVendidas * (bikePrice * 1.5);
      var lucro = ganho - empregados * (salMin + adicional) - bikeVendidas * bikePrice;
      setState(() {
        _resultado = 'Sálario final: ${salMin + adicional}\nLucro: $lucro';
      });
    } else {
      setState(() {
        _resultado = 'Por favor, insira números';
      });
    }
  }
 
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Rendimento do Taxi'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              TextField(
                controller: _empregados,
                decoration: const InputDecoration(
                  labelText: 'Digite a quantidade de empregados:',
                ),
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _salminimo,
                decoration: const InputDecoration(
                  labelText: 'Digite o valor do sálario mínimo:',
                ),
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _bikepreco,
                decoration: const InputDecoration(
                  labelText: 'Digite o preço da bike:',
                ),
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _bikevendida,
                decoration: const InputDecoration(
                  labelText: 'Digite a quantidade de bikes vendidas:',
                ),
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 20),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  // Botão CONVERTER com borda arredondada
                  FilledButton(
                    onPressed: _converter,
                    style: ButtonStyle(
                      shape: MaterialStateProperty.all(
                        RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(8),
                        ),
                      ),
                      padding: MaterialStateProperty.all(
                          const EdgeInsets.symmetric(horizontal: 40, vertical: 15)),
                    ),
                    child: const Text('CALCULAR'),
                  ),
                ],
              ),
              Container(
                padding: const EdgeInsets.all(16),
                margin: const EdgeInsets.only(top: 20),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Center(
                  child: Text(
                    _resultado.isEmpty
                        ? 'O Resultado aparecerá aqui'
                        : _resultado,
                    style: const TextStyle(
                      fontSize: 20,
                      color: Color(0xff000000),
                    ),
                    textAlign: TextAlign.center,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: false,
      ),
    );
  }
}