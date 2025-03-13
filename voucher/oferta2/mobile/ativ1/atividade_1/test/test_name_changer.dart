// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter_test/flutter_test.dart';
import 'package:atividade_1/aula01/name_changer.dart';

void main() {
  testWidgets('Counter increments smoke test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const NameChangerApp());

    // Verify that our counter starts at 0.
    expect(find.text('Mudar Nome'), findsOneWidget);
    expect(find.text('Elaias'), findsOne);

    // Tap the '+' icon and trigger a frame.
    await tester.tap(find.text('Mudar Nome'));
    await tester.pump();

    // Verify that our counter has incremented.
    expect(find.text('Elias'), findsOne);
  });
}
