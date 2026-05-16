import 'package:yemekhane/recommendation/data/model/recommendation_model.dart';
import 'package:yemekhane/recommendation/domain/entity/recommendation.dart';
import 'package:yemekhane/recommendation/domain/repository/i_recommendation_repository.dart';

class RecommendationRepository implements IRecommendationRepository {
  @override
  Future<List<Recommendation>> getRecommendations() async {
    await Future.delayed(Duration(seconds: 2)); // Simulate network delay

    final models = [RecommendationModel(answer: 'Flat White')];

    return models.map((model) => model.toEntity()).toList();
  }
}
