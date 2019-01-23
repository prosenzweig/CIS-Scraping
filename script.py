import requests

url = "https://downloads.cisecurity.org:443/download?hsCtaTracking=3e18967f-91ca-48b4-a05e-b9200a320a52%7Cc599ab8f-d7e4-4399-870c-a2b14d9a1754"
cookies = {"_ga": "GA1.2.56586678.1539727315", "_gid": "GA1.2.926563014.1539727315", "__hstc": "183371129.0009c1aa4969cc1abb033bd68aac9f3e.1539727315523.1539727315523.1539727315523.1", "__hssrc": "1", "__hssc": "183371129.3.1539727315523", "hubspotutk": "0009c1aa4969cc1abb033bd68aac9f3e", "utag_main": "v_id:01667ee661ba0007684ab633150b0305a002700d00978$_sn:1$_ss:0$_st:1539729178118$ses_id:1539727319487%3Bexp-session$_pn:3%3Bexp-session", "CISBenchmark": "Y", "cis_download_cookie": "HHcATjbrDA8hA2eZDHg5SyaTg7OGMDHBDnUeXgDF", "CookieConsent": "{stamp:'yQk92TexIya509OoIg4futt3aqs+YTfaK7Gv3Z9XTN3vGqkAVzYTyg=='%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1}", "_hjIncludedInSample": "1", "documentId": "235"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.3", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://downloads.cisecurity.org/?utm_campaign=Benchmarks&utm_medium=email&_hsenc=p2ANqtz-8GkQe1vmqgVJn7_L68C78BzmifQgfMoGRxeYxD8eJV3Y4P95VDYyliJaEqXp9EUJBfpDYVNKx8KITiA5fReGYSiXTy1w&_hsmi=35678746&utm_content=35678746&utm_source=hs_automation&hsCtaTracking=41ef8b02-d0e5-4acb-b542-67c919c7098e%7C500cec43-3dc4-4f4e-8680-465ba237fae1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}


for i in range(500,1000):
	cookies['documentId'] = str(i)
	response = requests.get(url, headers=headers, cookies=cookies)
	if response.status_code == 200:
		filename = response.headers['Content-Disposition'].split('"')[1]
		print(filename)
		with open(filename, 'wb') as f:
			f.write(response.content)
	else:
		break;
else:
	print("Fin du scraping")

