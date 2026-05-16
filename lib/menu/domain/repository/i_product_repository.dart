import 'package:yemekhane/menu/domain/entity/product.dart';

abstract class IProductRepository {
  Future<List<Product>> getProducts();
}
