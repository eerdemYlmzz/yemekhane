class Meal {
  final String id;
  final String date;
  final List<String> items;
  final List<String> calories;
  final int totalCalorie;

  Meal({
    required this.id,
    required this.date,
    required this.items,
    required this.calories,
    required this.totalCalorie,
  });

  factory Meal.fromFirestore(Map<String, dynamic> data, String id) {
    return Meal(
      id: id,
      date: data['date'] ?? '',
      items: List<String>.from(data['items'] ?? []),
      calories: List<String>.from(data['calories'] ?? []),
      totalCalorie: data['total_calorie'] ?? 0,
    );
  }
}
