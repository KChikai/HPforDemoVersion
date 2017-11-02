from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import io
from .models import New, Paper, Author
from . import APP_LABEL


def home(request):
    # 最新5件のニュースをデータベースから取得
    obj_latest_5 = New.objects.order_by('-date')[:5]
    context = {'latest_news_list': obj_latest_5}
    if len(context['latest_news_list']) == 0:
        return render(request, APP_LABEL + '/home.html')
    else:
        return render(request, APP_LABEL + '/home.html', context)


def research(request):
    return render(request, APP_LABEL + '/research.html')


def new(request):
    records = New.objects.exclude(text_ja="").order_by("-date")
    years = set(record.date.year for record in records)
    news = {year:[] for year in years}
    for record in records:
        news[record.date.year].append({
                "id": record.id, "date": str(record.date), "text_ja": record.text_ja, "image": record.image
            })
    news = sorted(news.items(), key=lambda x: -x[0])
    return render(request, APP_LABEL + '/new.html', context={"news":news})


def member(request):
    return render(request, APP_LABEL + '/member.html')


def paper(request):
    papers = Paper.objects.all()  # とりあえず論文オブジェクトをすべて取得
    queries = request.GET  # GETで検索条件を取得
    tmp_papers = []  # 検索結果候補の論文オブジェクトを入れておくリスト

    if "text_box" in queries and queries["text_box"]:
        # 検索ボックスの文字列で検索
        # 検索ワードをスペースで分割
        query_words = queries["text_box"].split()
        if queries["andor"] == "or":
            for paper in papers:
                # どれかの検索ワードが一つでもあてはまれば
                if any(paper.title.lower().find(query_word.lower()) != -1 for query_word in query_words):
                    tmp_papers.append(paper)
        else:
            for paper in papers:
                # すべての検索ワードがあてはまれば
                if all(paper.title.lower().find(query_word.lower()) != -1 for query_word in query_words):
                    tmp_papers.append(paper)
        papers = tmp_papers

    if "sorting" in queries:
        if queries["sorting"] == "year":
            # 発行年でソート
            papers = sorted(papers, key=lambda p: p.year)
        elif queries["sorting"] == "title":
            # タイトルでソート
            papers = sorted(papers, key=lambda p: p.title.lower())
        else:
            pass

    paper_groups = {}
    if "grouping" in queries:
        if queries["grouping"] == "none":
            paper_groups["全て"] = papers
        elif queries["grouping"] == "kaigi":
            for paper in sorted(papers, key=lambda p: p.colloquium):
                if paper.colloquium not in paper_groups:
                    paper_groups[paper.colloquium] = [paper]
                else:
                    paper_groups[paper.colloquium].append(paper)
        elif queries["grouping"] == "year":
            for paper in sorted(papers, key=lambda p: p.year):
                if paper.year not in paper_groups:
                    paper_groups[paper.year] = [paper]
                else:
                    paper_groups[paper.year].append(paper)
    else:
        paper_groups["全て"] = papers

    context = {
        'papers': papers,
        'paper_groups': paper_groups,
    }

    return render(request, APP_LABEL + '/paper.html', context)


def detail_paper(request, question_id):
    result = get_object_or_404(Paper, pk=question_id)
    return render(request, APP_LABEL + '/paper_detail.html', {'paper': result})


def detail_author(request, question_id):
    result = get_object_or_404(Author, pk=question_id)
    return render(request, APP_LABEL + '/author_detail.html', {'author': result})


def download_bibtex(request):
    papers = Paper.objects.all()
    queries = request.POST
    tmp_papers = []
    if "text_box" in queries and queries["text_box"]:
        # 検索ボックスの文字列で検索
        # 検索ワードをスペースで分割
        query_words = queries["text_box"].split()
        if queries["andor"] == "or":
            for paper in papers:
                # どれかの検索ワードが一つでもあてはまれば
                if any(paper.title.lower().find(query_word.lower()) != -1 for query_word in query_words):
                    tmp_papers.append(paper)
        else:
            for paper in papers:
                # すべての検索ワードがあてはまれば
                if all(paper.title.lower().find(query_word.lower()) != -1 for query_word in query_words):
                    tmp_papers.append(paper)
        papers = tmp_papers
    return download(papers)


def convert_paper(paper):
    bibtex = "@article{{\n \
    author=\"{author}\",\n \
    title=\"{title}\",\n \
    journal=\"{journal}\",\n \
    year=\"{year}\"".format(
        author="test author".strip(),
        title=paper.title.strip(),
        journal=paper.colloquium.strip(),
        year=str(paper.year).strip()
    )
    if paper.volume:
        bibtex += ",\nvolume=\"" + paper.volume.strip() + "\""
    if paper.number:
        bibtex += ",\nnumber=\"" + str(paper.number).strip() + "\""
    # if paper.pages:
    #    bibtex += ",\npages=" + paper.pages
    # if paper.month:
    #        bibtex += ",\nmonth=" + paper.month
    # if paper.note:
    #    bibtex += ",\nnote=" + paper.note
    return bibtex + "\n}"


def paper_to_bibtexes(papers):
    return '\n'.join(convert_paper(paper) for paper in papers)


def download(papers):
    output = io.StringIO()
    output.write(paper_to_bibtexes(papers))
    response = HttpResponse(output.getvalue(), content_type="text/plain")
    response["Content-Disposition"] = "filename=result.bib"
    return response


def _download(papers, queries):
    if queries['format'] == 'bibtex':
        output = io.StringIO()
        output.write(paper_to_bibtexes(papers))
        response = HttpResponse(output.getvalue(), content_type="text/plain")
        response["Content-Disposition"] = "filename=result.bib"
    elif queries['format'] == 'pdf':
        response = None
    return response