import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

Text styledText(
    {String txt = 'Mude-me',
    int? txtCor,
    FontWeight? fW,
    double? fS,
    FontStyle? fSt,
    int? bgCor,
    TextAlign? tA}) {
  return Text(
    txt,
    textAlign: tA ?? TextAlign.center,
    style: TextStyle(
        color: Color(txtCor ?? 0xFF000000),
        fontWeight: fW ?? FontWeight.w300,
        fontStyle: fSt ?? FontStyle.normal,
        fontSize: fS ?? 16,
        backgroundColor: Color(bgCor ?? 0x00ffFFFF)),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  static const String _title = 'Flutter Stateful Clicker Counter';
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        title: _title,
        theme: ThemeData(
          // useMaterial3: false,
          primarySwatch: Colors.blue,
        ),
        home: Scaffold(
            appBar: AppBar(
              title: styledText(
                  txt: 'Perfil do Usuário',
                  bgCor: 0x00aa00aa,
                  fS: 20,
                  txtCor: 0xffaa00aa,
                  fW: FontWeight.bold),
              backgroundColor: const Color(0xff65e831),
            ),
            body: Container(
              color: const Color(0xff000000),
              height: double.infinity,
              width: double.infinity,
              child: Center(
                child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      styledText(
                          txt: 'Joãozinho',
                          fS: 32,
                          txtCor: 0xff0000ff,
                          fW: FontWeight.bold),
                      const SizedBox(
                        height: 8,
                      ),
                      styledText(
                          txt: 'Idade: 22',
                          fS: 26,
                          txtCor: 0xffff0000,
                          fSt: FontStyle.italic),
                      const SizedBox(
                        height: 8,
                      ),
                      styledText(
                          txt: 'Cidade: Itú',
                          fS: 26,
                          txtCor: 0xffff00ff,
                          fSt: FontStyle.italic),
                      const SizedBox(
                        height: 8,
                      ),
                      const Image(
                          image: NetworkImage(
                              'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRIBBhhKd2Wct_igIwjHP9zaunCOUmZDi5rg&s')),
                      const SizedBox(
                        height: 16,
                      ),
                      const Text(
                        'Lizzard Doggo',
                        style: TextStyle(color: Color(0xFFFFFFFF)),
                      )
                    ]),
              ),
            )));
  }
}
