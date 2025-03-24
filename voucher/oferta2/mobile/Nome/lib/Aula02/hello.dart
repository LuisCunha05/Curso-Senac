import 'package:flutter/material.dart';

class OlaMundo extends StatelessWidget {
  const OlaMundo({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Meu Primeiro Programa',
      debugShowCheckedModeBanner: true,
      home: Text('Olá Mundoo'),
    );
  }
}
