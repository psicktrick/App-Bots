from __future__ import absolute_import
from celeryapp import app
import time
from datetime import datetime, timedelta
import HttpCalls
import os
import json

header = {"Content-Type": "application/json"}
like_api = "http://staging.womaniya.co:8080/video/api/rs/v2/service/post/like"
view_api = "http://staging.womaniya.co:8080/video/api/rs/v2/service/post/view"
comment_api = "http://staging.womaniya.co:8080/video/api/rs/v2/service/post/comment"
share_api = "http://staging.womaniya.co:8080/video/api/rs/v2/service/post/share"
follow_api = "http://staging.womaniya.co:8080/video/api/rs/v2/service/post/follow"


@app.task
def like(user_id, video_id, at):
    data = {
        "authToken": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjYzMCwibG9naW5JZCI6MTIxMiwicGxhdGZvcm0iOiIiLCJpYXQiOjE1NDI3MjIxNjksImV4cCI6MTU0NzkwNjE2OX0.xG3RTldZQYM4_I39Mi832_XvtAJrNaRGWPhBZPLJ2rQ",
        "videoId": video_id,
        "userId": user_id,
        "like": True
    }
    post = Http(like_api, json.dumps(data), header)
    r = post.post()
    # print(r)
    response = r.json()
    print("liked: {}".format(response['data']['success']))


@app.task
def view(user_id, video_id):
    data = {
        "authToken": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjYzMCwibG9naW5JZCI6MTIxMiwicGxhdGZvcm0iOiIiLCJpYXQiOjE1NDI3MjIxNjksImV4cCI6MTU0NzkwNjE2OX0.xG3RTldZQYM4_I39Mi832_XvtAJrNaRGWPhBZPLJ2rQ",
        "videoId": video_id,
        "userId": user_id,
    }
    post = Http(view_api, json.dumps(data), header)
    r = post.post()
    response = r.json()
    print("viewed: {}".format(response['data']['success']))


@app.task
def comment(user_id, video_id, comment="good"):
    data = {
        "authToken": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjYzMCwibG9naW5JZCI6MTIxMiwicGxhdGZvcm0iOiIiLCJpYXQiOjE1NDI3MjIxNjksImV4cCI6MTU0NzkwNjE2OX0.xG3RTldZQYM4_I39Mi832_XvtAJrNaRGWPhBZPLJ2rQ",
        "videoId": video_id,
        "userId": user_id,
        "comment": comment
    }
    post = Http(comment_api, json.dumps(data), header)
    r = post.post()
    response = r.json()
    print("commented: {}".format(response['data']['success']))


@app.task
def share(user_id, video_id):
    data = {
        "authToken": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjYzMCwibG9naW5JZCI6MTIxMiwicGxhdGZvcm0iOiIiLCJpYXQiOjE1NDI3MjIxNjksImV4cCI6MTU0NzkwNjE2OX0.xG3RTldZQYM4_I39Mi832_XvtAJrNaRGWPhBZPLJ2rQ",
        "videoId": video_id,
        "userId": user_id,
    }
    post = Http(share_api, json.dumps(data), header)
    r = post.post()
    response = r.json()
    print("shared: {}".format(response['data']['success']))


@app.task
def follow(user_id, video_id):
    data = {
        "authToken": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjYzMCwibG9naW5JZCI6MTIxMiwicGxhdGZvcm0iOiIiLCJpYXQiOjE1NDI3MjIxNjksImV4cCI6MTU0NzkwNjE2OX0.xG3RTldZQYM4_I39Mi832_XvtAJrNaRGWPhBZPLJ2rQ",
        "toFollow": user_id,
        "follow": True
    }
    post = Http(follow_api, json.dumps(data), header)
    r = post.post()
    response = r.json()
    print("followed: {}".format(response['data']['success']))


@app.task
def perform(user_id, video_id):

    t = datetime.utcnow()
    
    five_sec = t + timedelta(seconds=5)
    ten_sec = t + timedelta(seconds=10)
    twenty_sec = t + timedelta(seconds=20)
    like.apply_async((user_id, video_id), eta=five_sec)
    view.apply_async((user_id, video_id), eta=five_sec)
    comment.apply_async((user_id, video_id), eta=five_sec)
    share.apply_async((user_id, video_id), eta=five_sec)
    follow.apply_async((user_id, video_id), eta=five_sec)

    # for delayed_time in [five_sec, ten_sec, twenty_sec]:
    #     like.apply_async((user_id, video_id), eta=delayed_time)
    # comment.apply_async((user_id, post_id), eta = delayed_time)
    # share.apply_async((user_id, post_id), eta = delayed_time)
    # follow.apply_async((user_id, post_id), eta = delayed_time)

    # view.apply_async((user_id, video_id))
    # comment.apply_async((user_id, video_id))
    # like.apply_async((user_id, video_id))
    # share.apply_async((user_id, video_id))
    # follow.apply_async((user_id, video_id))
