import 'package:flutter/material.dart';
 
class Poupanca extends StatefulWidget {
  const Poupanca({super.key});

  @override
  _PoupancaState createState() => _PoupancaState();
}
 
class _PoupancaState extends State<Poupanca> {
  final TextEditingController _controller1 = TextEditingController();
  String _resultado = '';
 
  void _converter() {
    final num1 = double.tryParse(_controller1.text);
    const rendimento = 0.05;
    
    if (num1 != null) {
      setState(() {
        _resultado = 'Rendimento: ${num1 * rendimento}\nTotal: ${num1 * (1 + rendimento)} ';
      });
    } else {
      setState(() {
        _resultado = 'Por favor, insira um número válido em metros';
      });
    }
  }
 
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Rendimento do dinheiro em 1 mês na Poupança'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              TextField(
                controller: _controller1,
                decoration: const InputDecoration(
                  labelText: 'Digite o capital inicial:',
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