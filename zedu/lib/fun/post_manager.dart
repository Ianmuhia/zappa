import 'package:rxdart/rxdart.dart';
import 'post_service.dart';
import 'post_model.dart';

class PostManager {
  final PublishSubject<String> _filterSubject = PublishSubject<String>();
  final PublishSubject<List<PostModel>> _collectionSubject = PublishSubject<List<PostModel>>();

  Stream<List<PostModel>> get browse$ => _collectionSubject.stream;

  Sink<String> get inFilter => _filterSubject.sink;
  PostManager(){
    _filterSubject.switchMap((filter) async* {
      yield await PostService.browse();
    }).listen((collection){
      _collectionSubject.add(collection);
    });
}