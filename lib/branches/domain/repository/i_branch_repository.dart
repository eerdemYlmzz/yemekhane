import 'package:yemekhane/branches/domain/entity/branch.dart';

abstract class IBranchRepository {
  Future<List<Branch>> getBranches();
}
