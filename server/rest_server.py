from flask import Flask, jsonify, make_response, request
from flask import json
from flask_restful import Resource, Api, abort

from model.article_models import db, Article
from view.article_views import simple_article, list_articles


class ArticleService(Resource):

    def get(self, article_id):
        """
        Get an model.
        :return: Resource
        :type article_id: int
        """
        article = Article.query.get(article_id)
        if article:
            result = simple_article(article)
            code = 200
        else:
            result = {}
            code = 404
        return make_response(jsonify(result), code)

    def delete(self, article_id):
        """
        Delete an article.
        :param article_id: The id to delete
        :return: Resource
        """
        article = Article.query.get(article_id)
        if article:
            db.session.delete(article)
            db.session.commit()
            code = 204
        else:
            code = 404

        return None, code

    def put(self):
        """
        Create an article.
        """
        article_dict = json.loads(request.data)
        if article_dict.get('id'):
            abort(400)
        article = Article(article_dict['headline'], article_dict['body'])
        db.session.add(article)
        db.session.commit()
        result = simple_article(article)
        return make_response(jsonify(result), 200)

    def post(self):
        """
        Update an model.
        :return:
        """
        article_dict = json.loads(request.data)
        article_id = article_dict['id']
        article = Article.query.get(article_id)
        if article:
            article.headline = article_dict['headline']
            article.story_body = article_dict['body']
            db.session.commit()
            result = simple_article(article)
            code = 200
        else:
            result = {}
            code = 404
        return make_response(jsonify(result), code)


class ArticleServiceMeta(Resource):

    def get(self):
        articles = Article.query.all()
        return list_articles(articles)


def main():
    """
    Start the app server.
    :return:
    """
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ArticleServiceMeta, '/articles')
    api.add_resource(ArticleService, '/article/<int:article_id>', '/article')
    db.create_all()
    app.run(debug=True)
