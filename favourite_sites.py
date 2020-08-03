import requests, webbrowser

youtube_request = "coding+music" #change music
site_n1 = "https://automatetheboringstuff.com/2e/"
site_n2 = "https://google.com/"
site_n3 = "https://www.youtube.com/results?search_query="

webbrowser.open(site_n3+youtube_request)
webbrowser.open(site_n1)
webbrowser.open(site_n2)
