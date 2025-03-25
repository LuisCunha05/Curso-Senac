import 'package:flutter/material.dart';

class XShape extends StatelessWidget {

  final Color? cor;
  final bool? isX;

  const XShape({super.key, this.cor, this.isX});

  @override
  Widget build(BuildContext context) {
    return CustomPaint(
      size: const Size(100, 100),
      painter: isX != null ? XPainter( cor: cor) : OPainter(cor: cor),
    );
  }
}

class XPainter extends CustomPainter {
  final Color cor;

  XPainter({ Color? cor}) : cor = cor ?? Colors.black;

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = cor
      ..strokeWidth = 4.0
      ..style = PaintingStyle.stroke;
    
    // Draw first diagonal line (top-left to bottom-right)
    canvas.drawLine(const Offset(0, 0), Offset(size.width, size.height), paint);
    
    // Draw second diagonal line (top-right to bottom-left)
    canvas.drawLine(Offset(size.width, 0), Offset(0, size.height), paint);
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) => false;
}

class OPainter extends CustomPainter {
  final Color cor;
  final double width;
  final Size size;

  OPainter({
    Color? cor, 
    double? width,
  }) : cor = cor ?? Colors.black,
        width = width ?? 100,
        size = Size(width ?? 100, width ?? 100);

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = cor
      ..strokeWidth = 4.0
      ..style = PaintingStyle.stroke;
    
    size = this.size;
    double width = size.width;
    // Draw first diagonal line (top-left to bottom-right)
    canvas.drawCircle(const Offset(width, 0), size.width / 2, paint);
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) => false;
}