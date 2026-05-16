import 'package:yemekhane/branches/data/repository/branch_repository.dart';
import 'package:yemekhane/branches/domain/entity/branch.dart';

class GetBranchesUseCase {
  final _branchRepository = BranchRepository();

  Future<List<Branch>> call() async {
    return await _branchRepository.getBranches();
  }
}
