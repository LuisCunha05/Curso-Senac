import 'package:flutter/material.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text(
            'Perfil do Usuário',
            style: TextStyle(
              color: Colors.white, // Cor do texto
              fontWeight: FontWeight.bold, // Deixa o texto em negrito
            ),
          ),
          backgroundColor: Colors.purple,
        ),
        body: Container(
          color: Colors.black, // Cor do fundo da tela
          width:
              double.infinity, // Faz o container ocupar toda a largura da tela
          height:
              double.infinity, // Faz o container ocupar toda a altura da tela
          child: const Column(
            mainAxisAlignment: MainAxisAlignment.center, // Centraliza os textos
            crossAxisAlignment:
                CrossAxisAlignment.start, // Alinha os textos à esquerda
            children: [
              Text(
                'João Silva', // Nome do usuário
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold, // Texto em negrito
                  color: Colors.blue, // Cor do nome
                ),
              ),
              SizedBox(height: 10), // Espaço entre os textos
              Text(
                'Idade: 30 anos', // Idade do usuário
                style: TextStyle(
                  fontSize: 18,
                  fontStyle: FontStyle.italic, // Texto em itálico
                  color: Colors.red, // Cor da idade
                ),
              ),
              SizedBox(height: 10), // Espaço entre os textos
              Text(
                'Cidade: Campo Grande', // Cidade do usuário
                style: TextStyle(
                  fontSize: 18,
                  color: Colors.purple, // Cor da cidade
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
