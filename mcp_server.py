from fastmcp import FastMCP
from app import fetch_news
from app import generate_video_transcription

mcp = FastMCP("this is for real time news ")

@mcp.tool()
def fetch_new_mcp(query):
    return fetch_news(query=query)


@mcp.tool()
def gen_vid_trans_mcp(query):
    news = fetch_news(query=query)
    return generate_video_transcription(news)


if __name__ == "__main__":
    mcp.run()