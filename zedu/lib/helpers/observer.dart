import 'dart:async';
import 'package:flutter/material.dart';

class Observer<T> extends StatelessWidget{
  @required
  final Stream<T> stream;

  @required
  final Function onSuccess;
  final Function onWaiting;
  final Function onError;

  const Observer({this.onError, this.onSuccess, this.stream, this.onWaiting});

  Function get _defaultOnWaiting => (context) => Center(child: CircularProgressIndicator());
  Function get _defaultOnError => (context, error) => Text(error);

  @override
  Widget
}
