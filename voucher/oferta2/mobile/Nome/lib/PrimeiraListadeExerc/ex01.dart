import 'package:flutter/material.dart';
 
class Calcular extends StatefulWidget {
  @override
  _CalcularState createState() => _CalcularState();
}
 
class _CalcularState extends State<Calcular> {
  final TextEditingController _controller1 = TextEditingController();
  String _resultado = '';
 
  void _converter() {
    final num1 = double.tryParse(_controller1.text);
 
    if (num1 != null) {
      setState(() {
        _resultado = '${num1 * 100} cm';
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
          title: Text('Conversão de Metros para Centímetros'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              TextField(
                controller: _controller1,
                decoration: InputDecoration(
                  labelText: 'Digite a medida em metros:',
                ),
                keyboardType: TextInputType.number,
              ),
              SizedBox(height: 20),
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
                          EdgeInsets.symmetric(horizontal: 40, vertical: 15)),
                    ),
                    child: Text('CONVERTER'),
                  ),
                ],
              ),
              Container(
                padding: EdgeInsets.all(16),
                margin: EdgeInsets.only(top: 20),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Center(
                  child: Text(
                    _resultado.isEmpty
                        ? 'O Resultado aparecerá aqui'
                        : _resultado,
                    style: TextStyle(
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