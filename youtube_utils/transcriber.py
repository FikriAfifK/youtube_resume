from youtube_transcript_api import YouTubeTranscriptApi

video_id = "UtSSMs6ObqY"  

# Ambil transcript (subtitle)
try:
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id, languages=['en'])

    # is iterable
    # for snippet in fetched_transcript:
    #     print(snippet.text)

    # indexable
    last_snippet = fetched_transcript[-1]
    print("Last snippet:", last_snippet)
    # provides a length
    snippet_count = len(fetched_transcript)
    print("Total snippets:", snippet_count)

except Exception as e:
    print("Error:", e)
