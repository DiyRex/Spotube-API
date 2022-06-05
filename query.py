from youtube_search import YoutubeSearch


def search(keyword):
    base_url = "https://www.youtube.com/watch?v={0}"
    results = YoutubeSearch(keyword, max_results=1).to_dict()
    video_id = results[0]['id']
    video_link = base_url.format(video_id)
    return video_link

