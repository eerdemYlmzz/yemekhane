import 'package:yemekhane/menu/data/repository/product_repository.dart';
import 'package:yemekhane/menu/domain/entity/product.dart';

class GetProductsUseCase {
  final _productRepository = ProductRepository();

  Future<List<Product>> call() async {
    return await _productRepository.getProducts();
  }
}
