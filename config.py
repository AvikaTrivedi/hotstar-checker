from dotenv import load_dotenv

if os.path.exists("dangernetwork.env"):
    load_dotenv("dangernetwork.env")
else:
    load_dotenv()
