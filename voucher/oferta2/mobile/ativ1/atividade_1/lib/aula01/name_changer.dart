import 'dart:math';

import 'package:flutter/material.dart';

class NameChangerApp extends StatelessWidget {
  const NameChangerApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {

    return MaterialApp(
      title: 'Atividade 1',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text('Name changer'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ClipOval(child: Image(image: NetworkImage('https://static.vecteezy.com/system/resources/previews/033/501/239/non_2x/ai-generative-cartoon-portrait-of-a-person-on-transparent-background-png.png'),fit: BoxFit.cover, width: 120, height: 120,)),
            NameChanger(listaName: ['Elaias', 'Jão', 'Cadú', 'Luís', 'Junin'])
          ],
        ),
    )
    )
    );
  }
}

class NameChanger extends StatefulWidget {
  const NameChanger({super.key, required this.listaName});

  final List<String> listaName;

  @override
  State<NameChanger> createState() => _NameChangerState(listaName);
}

class _NameChangerState extends State<NameChanger> {

  final List<String> _list;
  String _text = '';
  
  _NameChangerState(this._list){
    _text = _list[0];
  }
  


  void _randomCounter() {
    setState(() {
      _text = _list[Random().nextInt(_list.length)];
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SizedBox(height: 8,),
        Text(_text),
        SizedBox(height: 16,),
        ElevatedButton(
          onPressed: _randomCounter,
          child: Text('Mudar Nome'),
        ),
      ],
    );
  }
}