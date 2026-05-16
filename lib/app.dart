import 'package:flutter/material.dart';
import 'package:yemekhane/home_screen.dart';

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Yemekhane',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        fontFamily: '.SF Pro Display', // San Francisco
        colorScheme: const ColorScheme.light(
          primary: Color(0xFFD32F2F),
          onPrimary: Colors.white,
          surface: Colors.white,
          onSurface: Colors.black,
        ),
        scaffoldBackgroundColor: Colors.transparent, // Arka plan Scaffold'dan ziyade HomeScreen'de gradient olacak
        appBarTheme: const AppBarTheme(
          backgroundColor: Colors.transparent,
          foregroundColor: Colors.white,
          centerTitle: true,
          elevation: 0,
        ),
        textTheme: const TextTheme(
          bodyLarge: TextStyle(color: Colors.black, fontFamily: '.SF Pro Display'),
          bodyMedium: TextStyle(color: Colors.black, fontFamily: '.SF Pro Display'),
          titleLarge: TextStyle(color: Colors.black, fontWeight: FontWeight.bold, fontFamily: '.SF Pro Display'),
        ),
      ),
      home: const HomeScreen(),
    );
  }
}
