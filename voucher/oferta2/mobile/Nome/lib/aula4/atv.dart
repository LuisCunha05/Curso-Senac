
import 'package:brasil_fields/brasil_fields.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';


class CadastroProduto extends StatelessWidget{

  final _c = TextEditingController();
  final _n = TextEditingController();
  final _p = TextEditingController();
  final _q = TextEditingController();
  final _r = TextEditingController();

  CadastroProduto({super.key});

  var _formulario = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(title: const Text('Cadastro Produto'),),
        body: Padding(padding: const EdgeInsets.all(16.0),
        child: Form(key: _formulario,
          child: Column(children: [
          TextFormField(
            controller: _c,
            decoration: const InputDecoration(labelText: 'Digite o Código'),
            keyboardType: TextInputType.number,
            inputFormatters: [FilteringTextInputFormatter.digitsOnly, LengthLimitingTextInputFormatter(6), ],
            validator: (value) {
              if(value == null || value.isEmpty){
                return "Insira um valor";
              }
              if(double.tryParse(value)! <= 0){
                return "Insira um valor maior que zero";
              }
              return null;
            },
          )
        , const SizedBox(height: 8, width: 8,),
        TextFormField(
            controller: _n,
            decoration: const InputDecoration(labelText: 'Digite o Nome:'),
            keyboardType: TextInputType.name,
            validator: (value) {
              if(value == null || value.isEmpty){
                return "Insira um valor";
              }
              if(value.length <= 3){
                return  "Insira uma palavra maior";
              }
              return null;
            },
          ),const SizedBox(height: 8, width: 8,),
          TextFormField(
            controller: _p,
            decoration: const InputDecoration(labelText: 'Digite o Preço'),
            keyboardType: TextInputType.number,
            inputFormatters: [FilteringTextInputFormatter.digitsOnly, LengthLimitingTextInputFormatter(6), CentavosInputFormatter(casasDecimais: 2)],
            validator: (value) {
              if(value == null || value.isEmpty){
                return "Insira um valor";
              }
              if(UtilBrasilFields.converterMoedaParaDouble(value) <= 0){
                return "Insira um valor maior que zero";
              }
              return null;
            },
          )
        , const SizedBox(height: 8, width: 8,),
        TextFormField(
            controller: _q,
            decoration: const InputDecoration(labelText: 'Digite o Quantidade:'),
            keyboardType: TextInputType.number,
            inputFormatters: [FilteringTextInputFormatter.digitsOnly, LengthLimitingTextInputFormatter(6), CentavosInputFormatter(casasDecimais: 2)],
            validator: (value) {
              if(value == null || value.isEmpty){
                return "Insira um valor";
              }
              if(UtilBrasilFields.converterMoedaParaDouble(value) <= 0){
                return "Insira um valor maior que zero";
              }
              return null;
            },
          )
        , const SizedBox(height: 8, width: 8,),
          TextField(
            maxLines: 5,
            controller: _r,
            decoration: const InputDecoration(labelText: 'Resultado:'),
            readOnly: true,
          ),const SizedBox(height: 8, width: 8,),
          Row(children: [
            FilledButton(onPressed: () {
              if(_formulario.currentState!.validate()){
                _r.text = "Produto Cadastrado!\nNome: ${_n.text}\nCódigo: ${_c.text}\nPreço: ${_p.text}\nQuantidade: ${_q.text}";
              }
              
          }, child: const Text('Cadastrar')),
            const SizedBox(height: 8, width: 8,),
            FilledButton(onPressed: () {
                _c.text = '';
                _n.text = '';
                _p.text = '';
                _q.text = '';
                _r.text = '';
            }, child: const Text('Limpar')),
          ],
      ) ],)) 
        ,),
      ),
    );
  }
}