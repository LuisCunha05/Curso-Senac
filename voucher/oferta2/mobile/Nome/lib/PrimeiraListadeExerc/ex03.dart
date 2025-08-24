import 'package:flutter/material.dart';
 
class TaxiCalculator extends StatefulWidget {
  const TaxiCalculator({super.key});

  @override
  _TaxiCalculatorState createState() => _TaxiCalculatorState();
}
 
class _TaxiCalculatorState extends State<TaxiCalculator> {
  final TextEditingController _ini = TextEditingController();
  final TextEditingController _fin = TextEditingController();
  final TextEditingController _lin = TextEditingController();
  final TextEditingController _din = TextEditingController();
  String _resultado = '';
 
  void _converter() {
    final ini = double.tryParse(_ini.text);
    final fin = double.tryParse(_fin.text);
    final litros = double.tryParse(_lin.text);
    final dinheiro = double.tryParse(_din.text);
    const precoGasosa = 2.5;
    
    if (ini != null && fin != null && litros != null && dinheiro != null) {
      var rodado = fin - ini;
      var media = rodado / litros;
      var gasto = litros * precoGasosa;
      var ganho = dinheiro - gasto;
      setState(() {
        _resultado = 'Média de consumo(Km/l): $media\nLucro do dia: $ganho';
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
                controller: _ini,
                decoration: const InputDecoration(
                  labelText: 'Digite a quilometragem inicial:',
                ),
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _fin,
                decoration: const InputDecoration(
                  labelText: 'Digite a quilometragem final:',
                ),
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _lin,
                decoration: const InputDecoration(
                  labelText: 'Digite a quantidade de gasolina gasta:',
                ),
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _din,
                decoration: const InputDecoration(
                  labelText: 'Digite a valor total ganho:',
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
                      shape: WidgetStateProperty.all(
                        RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(8),
                        ),
                      ),
                      padding: WidgetStateProperty.all(
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