

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';


class Formatador extends StatelessWidget{

  final _n1 = TextEditingController();
  final _n2 = TextEditingController();
  final _r = TextEditingController();

  Formatador({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Calculadora'),),
        body: Padding(padding: const EdgeInsets.all(16.0),
        child: Column(children: [
          TextField(
            controller: _n1,
            decoration: const InputDecoration(labelText: 'Digite o 1º Número:'),
            keyboardType: TextInputType.number,
            inputFormatters: [FilteringTextInputFormatter.digitsOnly, LengthLimitingTextInputFormatter(5)],
          )
        , const SizedBox(height: 8, width: 8,),
        TextField(
            controller: _n2,
            decoration: const InputDecoration(labelText: 'Digite o 2º Número:'),
            keyboardType: TextInputType.number,
            inputFormatters: [FilteringTextInputFormatter.digitsOnly, LengthLimitingTextInputFormatter(5)],
          ),const SizedBox(height: 8, width: 8,),
          TextField(
            controller: _r,
            decoration: const InputDecoration(labelText: 'Resultado:'),
            readOnly: true,
          ),const SizedBox(height: 8, width: 8,),
          Row(children: [
            FilledButton(onPressed: () {
              var x = double.tryParse(_n1.text) ?? 0.0;
              var y = double.tryParse(_n2.text) ?? 0.0;
              _r.text = (x + y).toString();
          }, child: const Text('Somar')),
            const SizedBox(height: 8, width: 8,),
            FilledButton(onPressed: () {
                _n1.text = '';
                _n2.text = '';
                _r.text = '';
            }, child: const Text('Limpar')),
          ],
       ) ],),),
      ),
    );
  }
}