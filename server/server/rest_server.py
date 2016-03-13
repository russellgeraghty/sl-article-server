from flask import Flask
from flask_restful import Resource, Api
from article.articles import db, Article

app = Flask(__name__)
api = Api(app)


class ArticleService(Resource):

    def get(self, article_id):
        article = Article.query.get(article_id)
        if article:
            result = {"id": article.id, "headline": article.headline, "body": article.story_body}
            response = 200
        else:
            result = {}
            response = 404
        return result, response


class ArticleServiceMeta(Resource):

    def get(self):
        articles = Article.query.all()
        result = []

        for a in articles:
            article = {"id": a.id, "headline": a.headline}
            result.append(article)

        return result


api.add_resource(ArticleServiceMeta, '/articles')
api.add_resource(ArticleService, '/articles/<int:article_id>')

if __name__ == '__main__':
    db.create_all()
    article = Article("Headline", "Cat does something")
    db.session.add(article)
    db.session.commit()
    app.run(debug=True)
