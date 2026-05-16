import 'package:yemekhane/market/domain/entity/catalog_product.dart';

abstract class IMarketRepository {
  Future<List<CatalogProduct>> getCatalogProducts();
}
