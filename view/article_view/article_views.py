def simple_article(article, decorate=None):
    """
    Convert an article into a dictionary suitable for making into JSON.
    :type decorate: dict
    :type article: article_model.article_models.Article
    :param article: The article
    :param decorate: In case you wish to decorate an existing view.
    :return: A dictionary view
    """
    if not decorate:
        decorate = {}
    decorate.update( {"id": article.id, "headline": article.headline, "body": article.story_body} )
    return decorate


def list_articles(articles):
    """
    Render a list of articles as a list of dictionaries.
    :type articles: list
    :param articles: The articles
    :return: List of dict
    """
    result = []
    if articles:
        for a in articles:
            article = {"id": a.id, "headline": a.headline}
            result.append(article)

    return result
