

def main():
	import time
	from InstagramAPI.InstagramAPI import InstagramAPI
	username = input("Give username: \t")
	password = input("Give password: \t")
	hashtag = input("Give hashtag: \t")


	api = InstagramAPI(username, password)
	api.login()

	feed = api.getHashtagFeed(hashtag, maxid='')
	results = api.LastJson

	while True:
		try:
			next_max_id = results["next_max_id"]
		except:
			next_max_id = None
		for r in results["items"]:
			like = api.like(r["id"])
		if next_max_id:
			feed = api.getHashtagFeed(hashtag, maxid=next_max_id)
			results = api.LastJson
		else:
			print("All Images liked. Bye!")
			quit()

if __name__ == "__main__":
	try:
		main()
	except Exception as E:
		print(E)
		time.sleep(60)

