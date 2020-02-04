class PostModel {
  final int id;
  final String title;
  final String body;
  final String postedtime;

  PostModel.fromJson(Map<String, dynamic> json)
    : id = json['id'] as int,
      title = json['title'],
      body = json['body'],
      postedtime = json['posted_time'];
}