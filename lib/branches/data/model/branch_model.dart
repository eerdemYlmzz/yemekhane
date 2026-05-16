import 'package:yemekhane/branches/domain/entity/branch.dart';

class BranchModel {
  final String? name;

  BranchModel({this.name});

  Branch toEntity() {
    return Branch(name: name);
  }
}
