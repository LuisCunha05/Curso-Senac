import 'package:flutter/material.dart';

class Calculadora extends StatefulWidget {
  @override
  _CalculadoraState createState() => _CalculadoraState();
}

class _CalculadoraState extends State<Calculadora> {
  final TextEditingController _controller1 = TextEditingController();
  final TextEditingController _controller2 = TextEditingController();
  String _resultadosoma = '';
  String _resultadosub = '';

  void _somar() {
    final num1 = double.tryParse(_controller1.text);
    final num2 = double.tryParse(_controller2.text);

    if (num1 != null && num2 != null) {
      setState(() {
        _resultadosoma = (num1 + num2).toString();
      });
    } else {
      setState(() {
        _resultadosoma = 'Por favor, insira números válidos';
      });
    }
  }

  void _sub() {
    final num1 = double.tryParse(_controller1.text);
    final num2 = double.tryParse(_controller2.text);

    if (num1 != null && num2 != null) {
      setState(() {
        _resultadosub = (num1 - num2).toString();
      });
    } else {
      setState(() {
        _resultadosub = 'Por favor, insira números válidos';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Calculadora'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              TextField(
                controller: _controller1,
                decoration: const InputDecoration(
                  labelText: 'Digite o primeiro número',
                ),
              ),
              TextField(
                controller: _controller2,
                decoration: const InputDecoration(
                  labelText: 'Digite o segundo número',
                ),
              ),
              const SizedBox(height: 20),
              FilledButton(
                onPressed: _somar,
                child: const Text('+'),
              ),
              const SizedBox(height: 20),
              FilledButton(
                onPressed: _sub,
                child: const Text('-'),
              ),
              TextField(
                decoration: const InputDecoration(
                  labelText: 'Resultado da soma',
                ),
                readOnly: true,
                controller: TextEditingController(text: _resultadosoma),
              ),
              TextField(
                decoration: const InputDecoration(
                  labelText: 'Resultado da subtração',
                ),
                readOnly: true,
                controller: TextEditingController(text: _resultadosub),
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
