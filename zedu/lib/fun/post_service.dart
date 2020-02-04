
import 'package:zedu/fun/post_model.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';


class PostService {

  String _url = "url_to_my-api";
  //GET POST
  static Future<List<PostModel>> browse() async {
    http.Response response = await http.get("$_url");
    String payload = response.body;

    List collection = json.decode(payload);

    Iterable<PostModel> elements = collection.map((_)=> PostModel.fromJson(_));
    return elements.toList();
  }

  //GET POST:ID
  static Future<PostModel> fetch(){}
}